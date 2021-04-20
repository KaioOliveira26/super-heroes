from django.urls import path
from .views import UserView, UserCreateView

urlpatterns = [
    path('',UserView.as_view()),
    path('create/', UserCreateView.as_view())
]