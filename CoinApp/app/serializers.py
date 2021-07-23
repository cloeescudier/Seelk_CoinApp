from rest_framework import serializers

from .models import ValueAlert, PercentageAlert, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ValueAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValueAlert
        fields = '__all__'

class PercentageAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = PercentageAlert
        fields = '__all__'