from django.urls import path
from . import views

#/user/ dizininden sora url yapısı
urlpatterns = [
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
]