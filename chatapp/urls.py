from . import views
from django.urls import path

urlpatterns = [
    path('', views.intro, name = 'intro'),
    path('', views.chat, name = 'chat'),
]
