from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    tel = serializers.CharField(
        max_length=30,
        validators=[RegexValidator(regex=r"(\+7|[8]|)?([9])([0-9]{9})")]
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'second_name', 'tel')
