#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/25/2020  10:45 PM 
# 文件名称   ：urls.py
from django.urls import path, re_path

from app01.views import user_auth, host


# app01应用路由配置
urlpatterns = [
    re_path(r'^register/$', user_auth.register, name='register'),
    re_path(r'^activate/(?P<token>.*)/$', user_auth.active_user, name='active'),
    # 登录
    re_path(r'^login/$', user_auth.login, name='login'),
    # 注销
    re_path(r'^logout/$', user_auth.logout, name='logout'),
    re_path(r'^index/$', user_auth.index, name='index'),

    # 主机信息
    re_path(r'^host/list/', host.host_list, name='host_list'),
]
