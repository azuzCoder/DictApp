from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('delete_img/', views.delete_profile_image, name='delete-profile-image'),


    path('password_reset', views.password_reset, name='password-reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'),
         name='password-reset-done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html',
                                                     success_url=reverse_lazy("users:password-reset-complete")),
         name='password-reset-confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),
         name='password-reset-complete'),


    # path('profile/update/', views.user_update_view, name='update-user')
]