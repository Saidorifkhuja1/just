from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'phone_number', 'name',
         'is_active', 'is_admin', 'is_superuser'
    )
    list_filter = ('is_active', 'is_admin', 'is_superuser')

    fieldsets = (
        ('Personal info', {
            'fields': ('phone_number', 'password', 'name',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone_number', 'name',
                'password1', 'password2',
                'is_active', 'is_admin', 'is_superuser'
            ),
        }),
    )

    search_fields = ('phone_number','name',)
    ordering = ('phone_number',)
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(User, UserAdmin)
