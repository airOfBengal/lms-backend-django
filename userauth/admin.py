from django.contrib import admin
from userauth.models import CustomUser, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "date"]


admin.site.register(CustomUser)
admin.site.register(Profile)
