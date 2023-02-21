from django.urls import path

from .views import HeroView, HeroListView

app_name = 'hero'

urlpatterns = [
    path('hero/', HeroView.as_view(), name='hero_view'),
    path('hero/list/', HeroListView.as_view(), name='hero_list')
]
