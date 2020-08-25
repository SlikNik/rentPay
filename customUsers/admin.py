from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from customUsers.models import MyUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'age',
                    'displayname',
                    'homepage',
                ),
            },
        ),
    )

admin.site.register(MyUser, CustomUserAdmin)
