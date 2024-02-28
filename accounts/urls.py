from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('singup/', views.UserRegistrationView.as_view(), name = 'singup'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('pass_change/', views.pass_change, name='passchange'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordChangeDoneView.as_view(template_name='reset_password_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),


    
]