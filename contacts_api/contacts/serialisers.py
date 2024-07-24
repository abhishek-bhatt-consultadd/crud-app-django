from rest_framework import serializers
from .models import Contact, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'  # Include all fields

class CategorySerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)  # Include related contacts

    class Meta:
        model = Category
        fields = '__all__'  # Include all fields

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
