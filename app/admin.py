# admin.py
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'address', 'email', 'image')
    # Add more fields as needed in the list_display
    search_fields = ['username', 'phone', 'email']
    # Add more fields as needed in the search_fields
