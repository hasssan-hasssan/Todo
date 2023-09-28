from django.urls import path
from app import views

urlpatterns = [
    path('', views.taskList, name='taskList'),
    path('<int:id>/edit/', views.taskUpdate, name='taskUpdate'),
    path('<int:id>/del/', views.taskDelete, name='taskDelete' ),
    path('new/', views.taskCreate, name='taskCreate'),
]
