from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index-page"),
    path('signup/',signup,name="signup-page"),
    path('login/',login,name="login-page"),
    path('success/',success,name="success-page"),
    path('logout/',logout,name="logout"),
    path('Profile/',Profile,name="Profile-Page"),
    path('LahoreFort/',LahoreFort,name="LahoreFort-Page"),
    path('Mohnjo/',Mohnjo,name="MonjoPic-Page"),
    path('Sheesh/',Sheesh,name="Sheesh-Page")
]


