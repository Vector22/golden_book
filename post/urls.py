from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import HomeView, user_login, LogoutView

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
