from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('group/create', views.group_form, name='group_form'),
    path('detail/<int:pk>/', views.group_detail, name='group_detail'),
    path('delete/<int:pk>/', views.group_delete, name='group_delete'),
]