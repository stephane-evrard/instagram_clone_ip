from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from PIL import Image

from django.forms.utils import flatatt


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'profile_pics/', blank=True, default='profile_pics/default.jpg')

    def save_profile(self):
        self.save()
        
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return f'self.user, self.bio, self.photo'
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
