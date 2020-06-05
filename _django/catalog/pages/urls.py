from django.urls import path
from . import views

#pages içerisindeki urls.py
#burada http://127.0.0.1:8000/ dizinine gelen istek ile hagi foksiyonun çalışacağını bildiriyoruz
urlpatterns = [
    path('', views.index, name='index'),
]