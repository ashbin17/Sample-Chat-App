from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


class Customuser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    nickname = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    pic = models.CharField(max_length=100)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='senderuser')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=1000)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
