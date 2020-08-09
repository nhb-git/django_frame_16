#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/26/2020  7:19 PM 
# 文件名称   ：tasks.py
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

from celery_tasks.main import app


@app.task
def send_activate_email(msg, to_email):
    text_content = '点击右边链接以完成激活，<a href="http://127.0.0.1:8000/activate/{{ token }}/">激活'
    msg_info = EmailMultiAlternatives(settings.SUBJECT, text_content, settings.EMAIL_FROM, to_email)
    msg_info.attach_alternative(msg.content.decode('utf-8'), 'text/html')
    msg_info.send()
