# from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_view, name="users"),
    path('users/create', views.create_account, name="create users"),
    path('auth/', views.login_view, name="login"),
    path('users/profile/', views.profile_view, name="profile"),
    path("users/verify_otp/", views.verify_otp),
    path("users/new_otp/", views.new_otp),

]