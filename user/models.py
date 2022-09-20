from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    bio = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', default="avatar.png", blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user}"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        print('profile created')

#post_save.connect(create_profile, sender=User)      s  

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if created == False:
       instance.profile.save()
       print('profile updated')

#post_save.connect(create_profile, sender=User)         