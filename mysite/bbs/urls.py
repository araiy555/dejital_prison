from django.views.generic import ListView, DetailView   #DetailViewをインポート
from django.urls import path
from . import views

app_name = 'bbs'
 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('comment/create/<int:id>/', views.comment, name='comment'),
    path('search', views.search, name='search'),
]
