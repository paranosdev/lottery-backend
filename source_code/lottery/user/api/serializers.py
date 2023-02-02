from django.db import transaction
from rest_framework import serializers
from user.models import User


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'display_name', 'email', 'username'
        ]
        extra_kwargs = {
            'username': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        raise NotImplementedError()

    @transaction.atomic
    def update(self, instance, validated_data):
        return super(UserInfoSerializer, self).update(instance, validated_data)
