from django.urls import path
from .views import CharacterListView, CharacterDetailView


urlpatterns = [
    path('', CharacterListView.as_view()),
    path('<int:pk>/', CharacterDetailView.as_view())
]
