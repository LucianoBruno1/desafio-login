from django.urls import path
from users.views import register, LoginAction, LogoutAction, home

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginAction, name='login'),
    path('logout/', LogoutAction, name='logout'),
    path('home/', home, name='home'),
]