from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('signin/', views.signin, name='signin'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]
