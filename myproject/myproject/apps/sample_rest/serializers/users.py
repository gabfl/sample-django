from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from ..models.users import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    email = serializers.CharField(
        required=False, allow_blank=True, max_length=200)

    class Meta:
        model = User
        #list_serializer_class = UserListSerializer
        # fields = ('name', 'email')

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
        pass


class UserListSerializer(serializers.ListSerializer):
    child = UserSerializer()
