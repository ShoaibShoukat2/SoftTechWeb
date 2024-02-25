from django.db import models

# Create your models here.


# models.py

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    password = models.CharField(max_length=255)
    # Add more fields as neededs


    def __str__(self):
        return self.username