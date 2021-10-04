from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (CustomUserCreationForm, CustomUserChangeForm)
from .models import (CustomUser, Game, Category, Transaction)


class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'is_staff', 'is_active','id')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None,{'fields':('username','email', 'password',)}),
        ('Permissions', {'fields' : ('is_staff','is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide', ),
            'fields': ('email', 'password1', 'password2','first_name','last_name', 'is_staff',)
            }
        
        ),
    )
    search_fieds = ('email', )
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Transaction)