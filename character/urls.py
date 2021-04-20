from django.urls import path
from .views import CharacterListView, CharacterDetailView,FavoriteCharacterView,FavoriteDetailView


urlpatterns = [
    path('', CharacterListView.as_view()),
    path('<int:pk>/', CharacterDetailView.as_view()),
    path('favorites/', FavoriteCharacterView.as_view()),
    path('favorites/<int:pk>',FavoriteDetailView.as_view())
]
