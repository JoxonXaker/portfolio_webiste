from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'email', 'is_verified']
    list_display_links = ['username', 'phone_number', 'email']


admin.site.register(User, UserAdmin)
admin.site.register(Profession)
admin.site.register(Specialization)
admin.site.register(Additional)
admin.site.register(Language)
admin.site.register(UserProfessions)
admin.site.register(UserSpecialization)
admin.site.register(UserLanguages)
admin.site.register(UserAdditional)
