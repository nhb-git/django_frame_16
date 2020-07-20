#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/20/2020  8:07 AM 
# 文件名称   ：forms.py
from django import forms


class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang']
    ]
    user_name = forms.CharField(label='用户名', max_length=50, initial='niu')
    user_city = forms.ChoiceField(label='城市', choices=CITY)
    user_message = forms.CharField(label='你的意见', widget=forms.Textarea)
