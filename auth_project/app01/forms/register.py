#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/25/2020  11:05 PM 
# 文件名称   ：register.py
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


# 导入User模型表
from app01.models import User

# 项目配置
from auth_project import settings


class RegisterForm(forms.Form):
    """用户注册表单"""
    username = forms.CharField(
        label='用户名', max_length=32, required=True, error_messages={
            'max_length': '用户名最长32位字符',
            'required': '请提供用户名',
        }, widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '用户名'
            }
        )
    )
    email = forms.EmailField(
        label='邮箱', required=True, error_messages={
            'required': '请提供邮箱',
            'invalid': '请输入有效格式的邮箱',
        }, widget=widgets.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '邮箱'
            }
        )
    )
    mobile = forms.CharField(
        label='手机号', max_length=11, required=True, error_messages={
            'required': '请提供手机号',
            'max_length': '手机号最长是11位'
        }, widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '手机号码'
            }
        )
    )
    # password = forms.CharField(
    password = forms.RegexField(
        r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\%\^\&\*\(\)])[0-9a-zA-Z!@#$\%\^\&\*\(\)]{8,32}$',
        label='密码', min_length=5, max_length=20, required=True, error_messages={
            'min_length': '密码最少5位',
            'max_length': '密码最多20位',
            'required': '请提供密码',
            'invalid': '密码必须包含数字，字母、特殊字符',
        }, widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '密码'
            }
        )
    )
    re_password = forms.CharField(
        label='重复密码', min_length=5, max_length=20, required=True, error_messages={
            'min_length': '密码最少5位',
            'max_length': '密码最多20位',
            'required': '请提供密码',
        }, widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '重复密码'
            }
        )
    )
    captcha = CaptchaField(
        label='验证码', error_messages={
            'invalid': '请输入有效的验证码',
            'required': '请输入验证码'
        }
    )

    def clean_username(self):
        """校验注册的用户名是否已被注册"""
        user = self.cleaned_data.get('username')
        ret = User.objects.filter(username=user)
        if ret:
            raise ValidationError('用户已存在')
        return user

    def clean_email(self):
        """检查邮箱是否已被注册"""
        email = self.cleaned_data.get('email')
        ret = User.objects.filter(email=email)
        if ret:
            raise ValidationError('邮箱已被注册')
        return email

    def clean_mobile(self):
        """校验手机号是否已被注册"""
        mobile = self.cleaned_data.get('mobile')
        ret = User.objects.filter(mobile=mobile)
        if ret:
            raise ValidationError('手机号已被注册')
        return mobile

    def clean(self):
        """检查注册时两次密码的一致性"""
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd != re_pwd:
            self.add_error('re_password', '两次密码不一致')
        return self.cleaned_data
