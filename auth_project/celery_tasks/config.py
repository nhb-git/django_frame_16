#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/26/2020  7:08 PM 
# 文件名称   ：config.py
# celery配置文件
BROKER_URL = 'redis://192.168.137.131/2'
CELERY_RESULT_BACKEND = 'redis://192.168.137.131:6379/1'
# CELERY_TASK_SERIALIZER = 'msgpack'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_IMPORTS = ('email',)
