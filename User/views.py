from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import os

from User.models import User
from User.serializers import UserSerializer


class UserAPIView(APIView):
    def get(self, request) :
        u = User.objects.all()
        return Response({"users": UserSerializer(u, many=True).data})

    def post(self, request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


# Create your views here.
def login_view(request) :
    context = {'login_data_error': False,
               'register_data_error': False,
               'password_equity_error': False,
               'email_error': False,
               'invalid_data_error': False,
               'created': False,
               'email': None,
    }
    if request.method == 'POST' :
        if 'login' in request.POST:
            email = request.POST.get('email_login')
            password = request.POST.get('password_login')
            if not len(email) or not len(password) :
                context['login_data_error']=True
                context['email'] = email
                messages.success(request, ("Не все поля заполнены (логин)!"))
                return render(request, 'sign_in.html', context)
            user = authenticate(request, email = email, password = password)
            if user : 
                user.update(is_active=True)
                login(request, user)
                messages.success(request, ("Должно было прокатить (логин)!"))
                return redirect('/')
            else:
                context['invalid_data_error'] = True
                context['email'] = email
                messages.success(request, ("походу не прокатило (логин)!"))
                return render(request, 'sign_in.html', context=context)
        elif 'register' in request.POST:
            email = request.POST.get('email_register')
            password1 = request.POST.get('password_register')
            password2 = request.POST.get('password2_register')
            if not len(email) or not len(password1) or not len(password2):
                context['email']=email
                context['register_data_error']=True
                messages.success(request, ("Не все поля заполнены (регистр)!"))
                return render(request, 'sign_in.html', context)
            if password1 != password2 :
                context['password_equity_error']=True
                context['email']=email
                messages.success(request, ("Пароли не совпадают (регистр)!"))
                return render(request, 'sign_in.html', context)
            user=User.objects.create_user(email, password1)
            if user : 
                context['created'] = True
                user.update(is_active=True)
                messages.success(request, ("Зарегано (регистр)!"))
                return render(request, 'sign_in.html', context=context)
            else :
                context['email_error'] = True
                context['email']=email
                messages.success(request, ("Почта уже зарегистрирована (регистр)!"))
                return render(request, 'sign_in.html', context=context)
    return render(request, 'sign_in.html', context=context)

def logout_view(request) :
    logout(request)
    messages.success(request, ("You were Logged Out!")) 
    return redirect('/sign-in')

def profile_view(request) :
    return render(request, 'profile.html', {})

def alter_profile_view(request) :
    user=request.user
    nickname=None
    profile_description=None
    if request.method=='POST':
        if request.POST.get('nickname') :
            nickname=request.POST.get('nickname')
        if request.POST.get('profile_description') :
            profile_description=request.POST.get('profile_description')

        user.update(username=nickname, profile_description=profile_description)
        if len(request.FILES) != 0 :
            os.remove(user.profile_pic.path)
            user.profile_pic = request.FILES['profile_pic']
            user.save()
        messages.success(request, ("Успешно изменено!"))
        return render(request, 'profile.html', {})
    return render(request, 'alter_profile.html', {})