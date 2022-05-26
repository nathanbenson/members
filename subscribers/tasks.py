from celery import shared_task
import time
import logging
from members import settings
from subscribers.models import Subscriber, Provider
from django.db import IntegrityError

log = logging.getLogger('.'.join((settings.LOG_NAME.split('.')[0], __name__,)))

@shared_task
def create_subscriber_patch(sub_list):
    """Queue up tasks to upload the batch in sets of 10000 or less"""
    shortened_list = sub_list
    while len(sub_list) > 10000:
        shortened_list = sub_list[10000:]
        sub_list = sub_list[10000:]
        create_patch(shortened_list)
    create_patch(shortened_list)
    return True


@shared_task
def create_patch(sub_list):
    """Create the members with their new information."""
    for member in sub_list:
        try:
            firstName, lastName, phone_number, client_member_id, account_id = member
            sub = None

            if None in (firstName, lastName, phone_number, client_member_id):
                log.info("Missing member info, skipping line")
            else:
                try:
                    sub_result = list(Subscriber.objects.filter(
                        phone_number=phone_number, client_member_id=client_member_id))
                    if sub_result:
                        sub = sub_result[0]
                    if not sub:
                        sub = Subscriber.objects.create_subscriber(
                            first_name=firstName, last_name=lastName,
                            phone_number=phone_number, client_member_id=client_member_id
                        )
                        sub.save()
                    try:
                        provider = Provider.objects.create_provider(subscriber=sub,
                                                                    account_id=str(account_id))
                        provider.save()
                    except IntegrityError:
                        log.info("Provider and subscriber combo already exists, skipping.")
                        pass
                except IntegrityError as e:  # noqa Not expecting this to ever hit.
                    log.info("phone number or client member id already exists.")

        except Exception as e:  # noqa
            log.info("found exception {}".format(str(e)))
            pass

    return True


