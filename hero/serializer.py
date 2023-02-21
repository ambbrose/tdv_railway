from rest_framework.serializers import ModelSerializer

from .models import Hero

class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'
        depth = 2
