from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile
from django.core.exceptions import ObjectDoesNotExist

#here django automatically creats the user profile automatically once it is signaled
@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)


#here it automatically saves the profile
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        profile.objects.create(user=instance)








































