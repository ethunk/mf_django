from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home),
    path('article/<int:article_id>', views.article),
]
