#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/20/2020  8:07 AM 
# 文件名称   ：forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang']
    ]
    user_name = forms.CharField(
        label='用户名', max_length=50, initial='niu',
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '用户名'
            }
        )
    )
    user_city = forms.ChoiceField(
        label='城市', choices=CITY, widget=widgets.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    user_message = forms.CharField(
        label='你的意见', widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean_user_name(self):
        user = self.cleaned_data.get('username')
        raise ValidationError('用户名不存在')
