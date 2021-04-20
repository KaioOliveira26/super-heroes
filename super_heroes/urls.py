from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
