from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

admin.site.register(User, UserAdmin)

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pound', 'dog_breed', 'profile_added', 'status', 'urgency')
    search_fields = ['pound', 'dog_breed', 'urgency']
    list_filter = ('status', 'profile_added', 'urgency')