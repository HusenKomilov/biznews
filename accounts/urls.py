from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name='logout'),
    path('registration/', registration, name="registration"),
    path('profile/<int:user_id>/', profile, name="profile"),
    path('contact/', contacts, name="contact"),
]