from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from customUsers.models import MyUser

class CustomUserAdmin(UserAdmin): #resource: https://stackoverflow.com/questions/48011275/custom-user-model-fields-abstractuser-not-showing-in-django-admin/48013640 
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'EC:Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'displayname',
                    'age',
                    'street',
                    'apt',
                    'state',
                ),
            },
        ),
    )

admin.site.register(MyUser, CustomUserAdmin)
