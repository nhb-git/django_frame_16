#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/21/2020  1:52 PM 
# 文件名称   ：login.py
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    COLORS = [
        ['红', '红'],
        ['蓝', '蓝'],
        ['紫', '紫']
    ]
    username = forms.CharField(
        label='用户名', min_length=2, max_length=20, error_messages={
            'min_length': '用户名最少可以设置2位',
            'max_length': '用户名最长可以设置20位'
        }, widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '用户名'
            }
        )
    )

    user_color = forms.ChoiceField(
        label='幸运颜色', choices=COLORS, widget=widgets.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
