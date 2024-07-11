from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """serializes a name field to testing our APIview"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a User Profile object"""

    class Meta:
        model = models.UserProfile
        fields = ("id", "name", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        """Overwrite Create and Return a new user"""
        user = models.UserProfile.objects.create_user(
            name=validated_data["name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed item"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ("id", "user_profile", "status_text", "created_on")
        extra_kwargs = {"user_profile": {"read_only": True}}
