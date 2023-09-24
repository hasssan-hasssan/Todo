from django.urls import path
from app import views

urlpatterns = [
    path('', views.taskList, name='taskList'),
    path('<int:id>/', views.taskUpdate, name='taskUpdate')
]
