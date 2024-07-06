from django.contrib import admin
from profiles_api.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "is_active", "is_staff", "is_superuser"]
    search_fields = ["name"]
    ordering = ["id"]


admin.site.register(UserProfile, UserProfileAdmin)
