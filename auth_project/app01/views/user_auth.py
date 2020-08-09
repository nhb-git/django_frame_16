#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/25/2020  11:01 PM 
# 文件名称   ：user_auth.py
from django.shortcuts import HttpResponse, render, redirect, reverse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings

# 注册表单
from app01.forms.register import RegisterForm

# 登录表单
from app01.forms.login import LoginForm

# 用户模型
from app01.models import User
# 邮件发送模块
from celery_tasks.email.tasks import send_activate_email

# 初始化权限
from app01.services.init_permission import init_permission


def register(request):
    """注册函数"""
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 'app01/register.html', {'form': register_form})
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            user_info = {
                'username': register_form.cleaned_data.get('username'),
                'password': register_form.cleaned_data.get('password'),
                'email': register_form.cleaned_data.get('email'),
                'mobile': register_form.cleaned_data.get('mobile'),
                'is_active': False
            }
            user_obj = User.objects.create_user(**user_info)
            # 生成token供邮箱确认
            token = user_obj.generate_confirmation_token()
            msg = render(request, 'app01/activate_email.html', {'token': token, 'username': user_obj.username})
            send_activate_email.delay(msg, [user_obj.email])

            message_info = '账号已经注册成功，请前往邮箱进行激活。'
            messages.add_message(request, messages.INFO, message_info)
            return render(request, 'app01/register_after.html')
        else:
            return render(request, 'app01/register.html', {'form': register_form})


def active_user(request, token):
    if request.method == 'GET':
        result = User.check_activate_token(token)
        return HttpResponse(result)


def login(request):
    """登录页面"""
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'app01/login.html', {'form': login_form})
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get('email')
            username = User.objects.get(email=email).username
            user_info = {
                'username': username,
                'password': request.POST.get('password')
            }
            user_obj = auth.authenticate(**user_info)
            if user_obj:
                auth.login(request, user_obj)
                init_permission(request, user_obj)
                return redirect(reverse('app01:index'))
            else:
                messages.add_message(request, messages.WARNING, '账户或密码错误.')
                return render(request, 'app01/login.html', {'form': login_form})
        else:
            return render(request, 'app01/login.html', {'form': login_form})


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'app01/index.html')


@login_required(login_url=settings.LOGIN_URL)
def logout(request):
    auth.logout(request)
    return redirect('app01:login')
