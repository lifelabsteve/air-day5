from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['id', 'payload', 'user', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']