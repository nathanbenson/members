import logging
import simplejson
import datetime
import csv
import io

from rest_framework import status
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from subscribers.models import Subscriber, Provider
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser
from subscribers.tasks import create_subscriber_patch
from members import settings

log = logging.getLogger('.'.join((settings.LOG_NAME.split('.')[0], __name__,)))


class GetSubsByAccountId(APIView):
    """Return all subscribers by a given account id."""

    renderer_classes = (JSONRenderer,)

    def get(self, request, account_id):  # noqa request
        try:
            log.info("Received request to get Member with account_id: %s", account_id,
                     extra={'request_time': str(datetime.datetime.utcnow())})
            data = Provider.objects.filter(account_id=account_id)
            data = [
                {
                    "member": str(sub.subscriber),
                    "providers": [str(provider) for provider in sub.subscriber.providers.all()]
                }
                for sub in data]
            return Response(data=data,
                            status=status.HTTP_200_OK)
        except Provider.DoesNotExist:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)


class GetSubById(APIView):
    """Return subscriber by a given id."""

    renderer_classes = (JSONRenderer,)

    def get(self, request, id):  # noqa request
        try:
            log.info("Received request to get Member with id: %s", id,
                     extra={'request_time': str(datetime.datetime.utcnow())})
            data = Subscriber.objects.get(id=id)
            data = {
                "member": str(data),
                "providers": [str(provider) for provider in data.providers.all()]
            }
            return Response(data=data,
                            status=status.HTTP_200_OK)
        except Subscriber.DoesNotExist:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)


class GetSubByPhoneNumber(APIView):
    """Return subscriber by a given phone number."""

    renderer_classes = (JSONRenderer,)

    def get(self, request, phone_number):  # noqa request
        try:
            log.info("Received request to get Member with phone_number: %s", phone_number,
                     extra={'request_time': str(datetime.datetime.utcnow())})
            data = Subscriber.objects.get(phone_number=phone_number)
            data = {
                "member": str(data),
                "providers": [str(provider) for provider in data.providers.all()]
            }
            return Response(data=data,
                            status=status.HTTP_200_OK)
        except Subscriber.DoesNotExist:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)


class GetSubByClientMemberId(APIView):
    """Return subscriber by a given client member id."""

    renderer_classes = (JSONRenderer,)

    def get(self, request, client_member_id):  # noqa request
        try:
            log.info("Received request to get Member with client_member_id: %s", client_member_id,
                     extra={'request_time': str(datetime.datetime.utcnow())})
            data = Subscriber.objects.get(client_member_id=client_member_id)
            data = {
                "member": str(data),
                "providers": [str(provider) for provider in data.providers.all()]
            }
            return Response(data=data,
                            status=status.HTTP_200_OK)
        except Subscriber.DoesNotExist:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)


class CreateMember(APIView):
    """Creates a subscriber if it doesn't exist, otherwise it
    attempts to update the subs providers"""

    renderer_classes = (JSONRenderer,)

    def post(self, request):
        """This will Create a Member and if given, Tie together the providers it has, and return the
         created subscriber and its providers. """
        data = request.data
        log.info(simplejson.dumps({'Member Data Recieved.': data}))

        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        phone_number = data.get('phone_number', None)
        client_member_id = data.get('client_member_id', None)
        provider_info = data.get("provider_info", [])
        return create_member(first_name,last_name,phone_number,client_member_id,provider_info)


class SubscriberBatchProcess(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request):
        data_file = request.FILES['myfile']
        decoded_file = data_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        file_content = csv.reader(io_string, delimiter=',', quotechar='|')
        members = []
        for row in file_content:
            members.append(row)
        create_subscriber_patch.delay(members)
        return render(request, '/home/usrznd/PycharmProjects/members/subscribers/templates/subscriber_upload.html', {
            'upload_file': True
        })

    def get(self, request):
        return render(request, '/home/usrznd/PycharmProjects/members/subscribers/templates/subscriber_upload.html')


class GenerateRandomUserView(APIView):

    parser_classes = (JSONRenderer,)

    def post(self, request):
        total = 20
        return Response("It worked.", status.HTTP_201_CREATED)


def create_member(first_name, last_name, phone_number, client_member_id, provider_info):
    """Create a given member."""
    sub = None

    if None in (first_name, last_name, phone_number, client_member_id):
        return Response(data="Missing member info, please check data and try again.",
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        try:
            sub_result = list(Subscriber.objects.filter(
                phone_number=phone_number, client_member_id=client_member_id))
            if sub_result:
                sub = sub_result[0]
        except Exception:  # noqa Not expecting this to ever hit.
            pass
        if not sub:
            sub = Subscriber.objects.create_subscriber(
                first_name=first_name, last_name=last_name,
                phone_number=phone_number, client_member_id=client_member_id
            )
            sub.save()
        for provider_id in provider_info:
            try:
                provider = Provider.objects.create_provider(subscriber=sub,
                                                            account_id=str(provider_id))
                provider.save()
            except IntegrityError:
                log.info("Provider and subscriber combo already exists, skipping.")
                pass

    except IntegrityError as e:
        return Response(
            data="phone_number or client_member_id already exists on a different member.",
            status=status.HTTP_400_BAD_REQUEST)

    if sub:
        data = {
            "member": str(sub),
            "providers": [str(provider) for provider in sub.providers.all()]
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK)
    return Response(
        data="Subscriber not created.",
        status=status.HTTP_400_BAD_REQUEST)