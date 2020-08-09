#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/26/2020  7:08 PM 
# 文件名称   ：main.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_project.settings')
# 创建celery实例
app = Celery('djcelery')

# 加载celery配置文件
app.config_from_object('celery_tasks.config')

# 自动扫描任务
app.autodiscover_tasks(['celery_tasks.email'])
