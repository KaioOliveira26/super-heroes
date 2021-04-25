from django.test import TestCase
from django.contrib.auth.models import User
import tempfile

from .models import FavoriteCharacter, Character
from .serializers import UserSerializer, FavoriteSerializer
import sys

class CharacterModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        superman_image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        cls.superman = Character.objects.create(
            name='Super Homem',
            photo=superman_image,
            description='Homem de aço',
            universe='DC',
            height=1.95,
            weight=100,
            strength=10,
            speed=10
        )
        batman_image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        cls.batman = Character.objects.create(
            name='Batman',
            photo=batman_image,
            description='Homem Morcego',
            universe='DC',
            height=1.75,
            weight=80,
            strength=6,
            speed=5
        )

    def test_valid_information(self):
        self.assertIsInstance(self.superman.name, str)
        self.assertIsInstance(self.superman.description, str)
        self.assertIsInstance(self.superman.universe, str)
        self.assertIsInstance(self.superman.height, float)
        self.assertIsInstance(self.superman.weight, int)
        self.assertIsInstance(self.superman.strength, int)
        self.assertIsInstance(self.superman.speed, int)

    def test_character_info(self):
        self.assertEqual(self.batman.name, 'Batman')
        self.assertEqual(self.superman.name, 'Super Homem')

class FavoriteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user= User.objects.create_user('kaio',password='teste1234')
        cls.random= User.objects.create_user('random',password='teste1234')
        
        superman_image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        cls.superman = Character.objects.create(
            name='Superman',
            photo=superman_image,
            description='Homem de aço',
            universe='DC',
            height=1.95,
            weight=100,
            strength=10,
            speed=10
        )
        
        batman_image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        cls.batman = Character.objects.create(
            name='Batman',
            photo=batman_image,
            description='Homem Morcego',
            universe='DC',
            height=1.75,
            weight=80,
            strength=6,
            speed=5
        )
        cls.favorite_kaio = FavoriteCharacter.objects.create(user=cls.user,character=cls.batman)
        cls.favorite_random = FavoriteCharacter.objects.create(user=cls.user,character=cls.superman)

    def test_valid_info(self):
        self.assertEqual(self.favorite_kaio.character.name, 'Batman')
        self.assertEqual(self.favorite_random.character.name, 'Superman')
    
    
    