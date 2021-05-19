from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib import admin
# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')     #CASCADE: if user is deleted the profile data associated will also get deleted
#     country = CountryField(blank=True)
#     birthdate = models.DateField(null=True, blank=True)
#
#     def __str__(self):
#         return 'Profile of user: {}'.format(self.user.username)
#
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.Profile.save()