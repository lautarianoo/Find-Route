from django.urls import path
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('login/', login_view, name='login_user'),
    path('logout/', logout_view, name='logout_user'),
    path('register/', register_view, name='register_user')
]