from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blogs'


urlpatterns = [
    path('user-list/', views.user_list, name='user-list'),  
    path('user-info/<int:id>/', views.user_info, name='user-info'),
    path('user-update/<int:id>/update/', views.user_info_update, name='user-info-update'), 
    path('user-add/', views.user_add, name='user-add'),
    path('user-delete/<int:id>/', views.user_del, name='user-del'),
    url(r'^.*/$', views.custom404, name="error")
]
