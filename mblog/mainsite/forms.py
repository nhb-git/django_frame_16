#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/20/2020  8:07 AM 
# 文件名称   ：forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from .models import Post
from captcha.fields import CaptchaField


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


class PostForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        self.fields['captcha'].label = '确定你不是机器人'
        self.fields['captcha'].widget.attrs['placeholder'] = '请输入验证码'


    # def clean_body(self):
    #     pass
