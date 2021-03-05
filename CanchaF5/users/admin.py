from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Usuario


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None ,{'fields': ('email', 'password', 'first_name', 'surname', 'dni')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'surname', 'dni', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('dni',)


admin.site.register(Usuario, CustomUserAdmin)