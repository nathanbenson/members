# coding=utf-8
"""Management command for running the bulk ."""
import logging
import time

from datetime import timedelta

from django.conf import settings
from django.core.management import BaseCommand
from django.db.models import Q
from django.utils import timezone

from commons.data_cleaner import DataCleaner
from ordertracking.models import EventMessage

log = logging.getLogger('.'.join((settings.LOG_NAME.split('.')[0], __name__,)))


class EventMessageCleaner(DataCleaner):
    """A class for querying/cleaning up events that are no longer relevant."""
    def __init__(self, chunk_size=None, clean_threshold=None, *args, **kwargs):
        """Initialize the EventMessageCleaner"""
        super(EventMessageCleaner, self).__init__(chunk_size, *args, **kwargs)
        self._clean_threshold = clean_threshold or 30

    @property
    def clean_threshold(self):
        """The threshold in days from today for which an EventMessage is cleanable.

        For example, if 30, EventMessages 30 days or older are eligible for cleaning. This value is configurable
        via the EVENT_MESSAGE_CLEAN_THRESHOLD localsetting or the command line arguments.
        """
        return getattr(settings, 'EVENT_MESSAGE_CLEAN_THRESHOLD', self._clean_threshold)

    def _clean_event_messages(self):
        """Cleans up old EventMessages."""
        threshold = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0).astimezone() \
            - timedelta(days=self.clean_threshold)
        queryset = EventMessage.objects.filter(Q(status=EventMessage.COMPLETE) | Q(created__lte=threshold))
        cleanable_ids = self._get_ids_for_queryset(queryset)
        self.delete_chunks(EventMessage, cleanable_ids, self.chunk_size)

    def clean(self):
        """Executes the full clean operation for event message."""
        start = time.time()
        print('Starting EventMessage cleanup at {}'.format(timezone.now().isoformat()))
        self._clean_event_messages()
        print('Finished EventMessage cleanup at {}. Total time was {}s'.format(
            timezone.now().isoformat(), time.time() - start)
        )


class Command(BaseCommand):
    """Management command for bulk cleaning EventMessages that are completed or too old."""

    help = 'Bulk clean EventMessages that are completed or too old'

    def add_arguments(self, parser):
        """Add args"""
        parser.add_argument(
            '-c', '--chunk_size', type=int,
            help='The size of the chunks to split the cleanup tasks into'
        )

        parser.add_argument(
            '-t', '--threshold', type=int,
            help='The threshold in days from today for which an EventMessage is cleanable.'
        )

    def handle(self, *args, **options):
        """Handle the command"""
        chunk_size = options['chunk_size'] if 'chunk_size' in options else None
        clean_threshold = options['threshold'] if 'threshold' in options else None
        cleaner = EventMessageCleaner(chunk_size, clean_threshold)
        cleaner.clean()
