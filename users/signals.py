from django.db.models.signals import post_save ,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import profile

from django.core.mail import send_mail
from django.conf import settings
#@receiver(post_save,sender=User)
def createProfile(sender ,instance,created,**kwargs):
   if created:
        user=instance
        Profile=profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        subject='Welcom message:)'
        message='I am glad to see you in my website:)'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [Profile.email],
            fail_silently=False,
        )
        
        


def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user

    if created==False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()


def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()


post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=profile)
post_delete.connect(deleteUser,sender=profile)