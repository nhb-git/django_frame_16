#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/27/2020  12:54 PM 
# 文件名称   ：login.py
from django import forms
from django.forms import widgets
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True, error_messages={
            'invalid': '请输入有效的邮箱',
            'required': '请输入邮箱地址'
        },
        widget=widgets.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '邮箱地址'
            }
        )
    )
    password = forms.CharField(
        required=True, error_messages={
            'required': '请输入密码'
        },
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '密码'
            }
        )
    )
    captcha = CaptchaField(
        error_messages={
            'invalid': '请输入正确的验证码'
        }
    )
