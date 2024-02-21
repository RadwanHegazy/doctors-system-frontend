from .views.auth import login, logout
from .views.client import home, register
from .views.doctor import profile
from django.urls import path


urlpatterns = [
    path('auth/login/',login.LoginView,name='login'),
    path('auth/logout/',logout.LogoutView,name='logout'),

    path('',home.ClientHomeView,name='home'),
    path('profile/',profile.DoctorHome,name='profile'),
    path('register/<str:doc_id>/',register.RegisteWithDoctorView,name='register_with_doc'),
]