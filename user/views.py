from django.shortcuts import render, redirect, reverse
from blog.models import ReadList
from django.db.models import Count
from django.db.models.functions import ExtractDay, ExtractMonth
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib import auth
from django.contrib.auth.models import User
from .form import LoginForm, RegisterForm, ChangeNickNameForm
from .models import Profile

def login(request):
    """
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username,password=password)
    direct = request.META.get('HTTP_REFERER', '/home')
    if user is not None:
        auth.login(request, user)
        return redirect(direct)
    else:
        return render(request, 'error.html', {"message":"用户不存在", "redirect":direct})
    """

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context["login_form"] = login_form
    return render(request, "user/login.html", context)


def login_for_medal(request):
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():
        user = login_form.cleaned_data['user']
        auth.login(request, user)
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)


def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            newuser = User()
            newuser.username = reg_form.cleaned_data['username']
            newuser.email = reg_form.cleaned_data['email']
            newuser.set_password(reg_form.cleaned_data['password'])
            newuser.save()
            user = auth.authenticate(request, username=newuser.username, password=newuser.password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegisterForm()
    context = {}
    context["reg_form"] = reg_form
    return render(request, "user/register.html", context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))


def user_info(request):
    context = {}
    context['user'] = request.user
    return render(request, 'user/user_info.html', context)


def change_nickname(request):
    if request.method == 'POST':
        form = ChangeNickNameForm(request.POST, user = request.user)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            profile, created = Profile.objects.get_or_create(user = request.user)
            profile.nickname = nickname
            profile.save()
            return redirect('/user/user_info/')
    else:
        form = ChangeNickNameForm()

    context = {}
    context['form'] = form
    context['page_title'] = '修改昵称'
    context['form_title'] = '修改昵称'
    context['submit_display'] = '修改'
    return render(request, 'user/form.html', context)