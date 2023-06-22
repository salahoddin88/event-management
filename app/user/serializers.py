"""
    Serializers for the user API View
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserDetailsSeializer(serializers.ModelSerializer):
    """ User details serializer """
    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email'
        )
