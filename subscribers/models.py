from django.db import models


class SubscriberManager(models.Manager):
    def create_subscriber(self, first_name, last_name, phone_number, client_member_id):
        sub = self.create(first_name=first_name, last_name=last_name,
                          phone_number=phone_number, client_member_id=client_member_id)

        return sub


# Create your models here.
class Subscriber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    client_member_id = models.CharField(max_length=20, unique=True)

    objects = SubscriberManager()

    def __str__(self):
        return "{},{},{},{},{}".format(self.id, self.first_name, self.last_name,
                                       self.phone_number, self.client_member_id)


class ProviderManager(models.Manager):
    def create_provider(self, subscriber, account_id):
        provider = self.create(subscriber=subscriber, account_id=account_id)

        return provider


class Provider(models.Model):
    subscriber = models.ForeignKey('Subscriber', on_delete=models.CASCADE, related_name='providers')
    account_id = models.CharField(max_length=20)

    objects = ProviderManager()

    def __str__(self):
        return self.account_id

    class Meta:
        unique_together = ('subscriber', 'account_id')
