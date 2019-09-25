from rest_framework import serializers
from mud.models import User

# mud serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
