from django.urls import path
from app1 import views
urlpatterns = [
    
    path('',views.Home,name=''),
    path('login',views.Login_page,name='login'),
    path('signUp',views.Sign_up,name='signUp'),
]