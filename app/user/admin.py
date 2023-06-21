from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    
    
admin.site.register(User, UserAdmin)