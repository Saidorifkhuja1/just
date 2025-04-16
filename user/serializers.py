from rest_framework import serializers
from .models import User
from drf_extra_fields.fields import Base64ImageField



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=1)


    class Meta:
        model = User
        fields = ['uid', 'name','phone_number', 'password']
        read_only_fields = ['uid']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'phone_number', 'name']


class UserUpdateSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['uid', 'name', 'phone_number', 'is_admin']
        read_only_fields = ['uid', 'is_admin']






