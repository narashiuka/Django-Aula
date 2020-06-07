"""
Definition of urls for PrimeiroDjango.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('hello/<nome>/<int:idade>/', views.hello),
    path('soma/<int:num1>/<int:num2>/', views.soma),
    path('subtracao/<int:num1>/<int:num2>/', views.subtracao),
    path('multiplicacao/<int:num1>/<int:num2>/', views.multiplicacao),
    path('divisao/<int:num1>/<int:num2>/', views.divisao),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
