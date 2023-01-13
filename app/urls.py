from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('',views.city,name='views'),
    path('signupdata/',views.signupform,name='signupform'),
    path('loginform/',views.loginform,name='loginform'),
    #path('login/',views.CustomerRegistrationView.as_view(),name='studentform'),
   # path('accounts/loginform/', auth_views.LoginView.as_view(template_name='app/loginform.html',
    #authentication_form=LoginForm),name='login'),
    path('profile/',views.profileform,name='profileform'),
    path('logoutdata/',views.logoutform,name='logoutform'),
    path('changepassword/',views.changepassword,name='changepassword')

    
]