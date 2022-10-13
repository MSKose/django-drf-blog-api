from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Profile


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)    # receiver decorator take the signal (post_save in this case) and also the sender (User, in our case) as an argument
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)  
def save_profile(sender, instance, **kwargs): # this function makes sure that our profile is saved everytime the User object gets saved
    instance.profile.save()