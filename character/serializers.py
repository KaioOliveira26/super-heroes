from rest_framework import serializers
from .models import Character,FavoriteCharacter
from user.serializers import UserSerializer


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id','name', 'photo', 'description', 'universe',
                  'height',  'weight', 'strength', 'speed']


class FavoriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    character = CharacterSerializer()
    user = UserSerializer()
    class Meta:
        model = Character
        fields = ['id','character','user']
