from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Manager(User):
    class Meta:
        verbose_name = 'manager'
        verbose_name_plural = 'managers'

    def __str__(self):
        return f'Manager: {self.username}'


class Cashier(User):

    class Meta:
        verbose_name = 'cashier'
        verbose_name_plural = 'cashiers'

    def __str__(self):
        return f'Cashier: {self.username}'

# Create your models here.
