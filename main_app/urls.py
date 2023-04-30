from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('user_login/', views.signin, name='signin'),
    path('contact/', views.contact_us, name='contact_us'),
    path('user_logout/', views.user_logout, name='logout'),
    path('sign_up/', views.register, name='register'),
    path('uploaded_images/', views.uploaded_images, name='uploaded_images'),
    path('uploaded_videos/', views.uploaded_videos, name='uploaded_videos'),
]
