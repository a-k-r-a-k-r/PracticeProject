from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('users/', views.user_list, name='user-list'),  
    path('user-info/<id>/', views.user_info, name='user-info'),
    path('user-update/<id>/update/', views.user_info_update, name='user-info-update'), 
    path('user-add/', views.user_add, name='user-add'),
    path('user-delete/<id>/', views.user_del, name='user-del')
]
