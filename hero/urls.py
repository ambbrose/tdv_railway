from django.urls import path

from .views import hero

urlpatterns = [
    path('', hero)
]