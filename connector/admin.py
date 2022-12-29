from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Booking


# To enable cutomisation of admin dashboard view based on User fields added
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'is_pound',
                    'is_rescue',
                    'pound_official_name',
                    'rescue_official_name',
                    'county',
                ),
            },
        ),
    )

    list_display = ['username', 'is_staff', 'is_pound',
                    'pound_official_name', 'is_rescue',
                    'rescue_official_name', 'county',]


admin.site.register(User, CustomUserAdmin)


# To add Profile model to admin to enable management of entries
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'pound', 'dog_breed', 'profile_added', 'status',
                    'urgency')
    search_fields = ['pound', 'dog_breed', 'urgency']
    list_filter = ('status', 'profile_added', 'urgency')


# To add Booking model to admin to enable management of entries
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rescue', 'collection_date', 'phone_number',
                    'profile')
    search_fields = ['rescue']
