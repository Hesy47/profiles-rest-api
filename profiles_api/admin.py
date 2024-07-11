from django.contrib import admin
from profiles_api.models import UserProfile, ProfileFeedItem


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "is_active", "is_staff", "is_superuser"]
    search_fields = ["name"]
    ordering = ["id"]


class ProfileFeedItemAdmin(admin.ModelAdmin):
    list_display = ["id", "user_profile", "status_text","created_on"]
    search_fields = ["user_profile"]
    ordering = ["id"]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProfileFeedItem, ProfileFeedItemAdmin)
