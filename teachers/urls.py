from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('create/', views.teacher_form, name='teacher_form'),
    path('detile/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),
]

