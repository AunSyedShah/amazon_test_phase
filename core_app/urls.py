from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.signin, name='signin'),
    path('contact/', views.contact_us, name='contact_us'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.register, name='register'),
    path('uploaded_images/', views.uploaded_images, name='uploaded_images'),
    path('uploaded_videos/', views.uploaded_videos, name='uploaded_videos'),
    path('delete_image/<int:image_id>', views.delete_image, name="delete_image")
]
