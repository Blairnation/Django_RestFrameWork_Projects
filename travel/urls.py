from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.main_page, name = 'travel'),
   path('login/', views.login, name='login'),
   path('register/', views.register, name='register'),
   path('try/', views.tryer, name='tryer'),
]