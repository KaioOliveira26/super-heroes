from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication

from django_filters import rest_framework as filters

from .models import Character,FavoriteCharacter
from .serializers import CharacterSerializer, FavoriteSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

from user.serializers import UserSerializer
from user.services import validate_token_user


class CharacterListView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filterset_fields = ('name',)


class CharacterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class FavoriteCharacterView(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = FavoriteCharacter.objects.filter()
    serializer_class = FavoriteSerializer

    def get(self, request):
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])

        user_object = valid['user']
        favorites = FavoriteSerializer(FavoriteCharacter.objects.filter(user=user_object),many=True).data
        
        return Response(favorites)
        
    def create(self, request):
        try:
            character_id = request.data['character_id']
        except:
            return Response('Forneça um personagem',400)

        character_object = Character.objects.get(id=character_id)
        try:
            character_object = Character.objects.get(id=character_id)
        except:
            return Response('Personagem não encontrado',404)
        
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])

        user_object = valid['user']
        favorites = FavoriteCharacter.objects.filter(user=user_object)
        
        for favorite in favorites:
            if character_object == favorite.character:
                return Response('Personagem já favoritado',401) 
        
        data = request.data
        favorite = FavoriteSerializer(FavoriteCharacter.objects.create(character=character_object,user=user_object)).data
        return Response(favorite,201)

class FavoriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteCharacter.objects.all()
    serializer_class = FavoriteSerializer