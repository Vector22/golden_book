from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.user_register, name="register"),
    path('my-admin/', login_required(views.my_admin), name='my_admin'),
    path('user/<int:pk>/', login_required(views.UserDetail.as_view()),
         name='user_detail'),
    path('user/new/', login_required(views.UserCreate.as_view()),
         name='user_new'),
    path('user/edit/<int:pk>', login_required(views.UserUpdate.as_view()),
         name='user_edit'),
    path('user/delete/<int:pk>', login_required(views.UserDelete.as_view()),
         name='user_delete'),
]
