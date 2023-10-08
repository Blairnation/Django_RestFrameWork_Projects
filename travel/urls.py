from django.urls import path, include
from . import views
from .views import GoogleSignupView


urlpatterns = [
   path('', views.main, name = 'travel'),
   path('login/', views.login, name='login'),
   path('register/', views.register, name='register'),
   # path('try/', views.tryer, name='tryer'),
   path('signup/google/', GoogleSignupView.as_view(), name='google-signup'),
 
]