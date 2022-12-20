from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main),
    path('store', views.store),
    path('dic', views.dic),
    path('achievement', views.achievement),

    path('character', views.character),
    path('skills', views.skills),
    path('api/shop/', views.shopAPI.as_view()),
    path('api/item/', views.ItemAPI.as_view()),
]