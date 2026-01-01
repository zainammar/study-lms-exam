from django.contrib import admin
from django.urls import path, include
from accounts.views import LogoutGetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('exam.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutGetView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
