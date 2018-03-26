from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from ..models.users import User

"""
    Another solution for the code below would be to use 
    `serializers.Serializer` instead of `serializers.ModelSerializer`
    and re-declare all fields and their types

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    email = serializers.CharField(
        required=False, allow_blank=True, max_length=200)

    def create(self, validated_data):
        ...
"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')

    def create(self, validated_data):
        return UserSerializer()

    def validate_email(self, email):
        """
        Check that the blog post is about Django.
        """

        # print('validation!')

        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError("Invalid email.")
        else:
            return email

    def validate_name(self, name):
        return name

    def save():
        pass

    def create(self, validated_data):
        # return User.objects.create(**validated_data)

        pass

    def update(self, instance, validated_data):
        # instance.name = validated_data.get('name', instance.name)
        # instance.email = validated_data.get('email', instance.email)
        # instance.save()
        # return instance

        pass


class UserListSerializer(serializers.ListSerializer):
    child = UserSerializer()
