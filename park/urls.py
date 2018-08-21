from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_dates, name='post_dates'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/date', views.post_detail, name='post_detail'),
    path('post/update', views.post_update, name='post_update'),
]