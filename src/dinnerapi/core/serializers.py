from rest_framework import serializers
from .models import CLiente

# Serializers define the API representation.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome','idade']
