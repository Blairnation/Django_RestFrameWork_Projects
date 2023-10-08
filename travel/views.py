from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib .auth import login as auth_login, authenticate
from social_django.models import UserSocialAuth
from .models import Customer
from threading import Thread
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import RedirectView

# Create your views here.


class HandleNotification(Thread):

    def __init__(self, subject, message, recipient_list):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list
        Thread.__init__(self)

        
    def run(self):
        from_email = 'tonyblair246@gmail.com'
        send_mail(self.subject, self.message, from_email,self.recipient_list, fail_silently=True)

def main(request):
   if request.method == 'POST':
  #     gender = request.POST['gender']
  #     phone_num = request.POST['phone_num']
  #     id_num = request.POST['id_num']
      pin = request.POST['pin']

      if pin != '8457762':
         messages.error(request, 'Invalid Pin!!  \t Enter a Valid Pin')
         return redirect('travel')
      
  #     user = request.user
  #     customer, created = Customer.objects.get_or_create(user=user, gender=gender,
  #                                               phone_num=phone_num,id_num=id_num)
  #     customer.save()
      messages.success(request, 'Verification Complete!! Account Booked')
  #     HandleNotification('Message From Nation Travel and Tour', 'Account Verificationomplete', [f'{user.email}',]).start()
      return redirect('travel')

   return render(request, 'try.html', {})

def login(request):
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)

      if user is not None:
         auth_login(request, user)
         messages.success(request, 'Login Successful')
         return redirect('travel')
      else:
         messages.error(request, 'Username Or Password Incorrect!!')
         return redirect('login')

   return render(request, 'login.html', {})

def register(request):
   if request.method == "POST":
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']


      if User.objects.filter(username=username):
         messages.error(request, 'Username Already Exists!! Try Another.')
         return redirect('register')
      
      if User.objects.filter(email=email):
         messages.error(request, "Email ALready Exists!!")
         return redirect('register')
      
      if password != password2:
         messages.error(request, "Password Doesn't Match!!")
         return redirect('register')
      
      
      user = User.objects.create_user(username=username,
                                      email=email,
                                      password=password)
      user.save()
      messages.success(request, 'Account Registered Succesfully')
      return redirect('login')

   return render(request, 'register.html', {})



def signup_with_google(request):
    # Redirect to Google authentication
    return redirect('social:begin', 'google-oauth2')

def signup_with_facebook(request):
    if request.user.is_authenticated:
        # User is already authenticated, handle this as needed
        return redirect('travel')
    else:
        # Redirect to Facebook authentication
        return render(request, 'register.html')
    

class GoogleSignupView(RedirectView):
    url = reverse_lazy('socialaccount_signup', args=['google'])
