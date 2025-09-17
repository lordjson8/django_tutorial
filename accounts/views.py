from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.views import generic,View
from django.http import HttpResponse
from .forms import LoginForm,RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'


class LoginView(View):
    form_class = LoginForm
    success_url = reverse_lazy('post')
    template_name = 'accounts/login.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        name= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        # print('user : ',username,password)
        if user is not None:
            print(messages.SUCCESS)

            print("user")
            login(request, user)
            return redirect(self.success_url)
        
        messages.error(request, 'Invalid Credentials')
        return redirect('login')
    

class SignUpView(View):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        username= request.POST.get('username')
        password= request.POST.get('password')
        cpassword= request.POST.get('confirmation_password')

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken")
            return redirect('signup')

        if cpassword != password:
            messages.error(request,"Password and confirmation password does not match")
            return redirect('signup')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        
        messages.success(request,"User created")

        return redirect('login')

    