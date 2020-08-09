#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/9/2020  8:15 PM 
# 文件名称   ：host.py
from django.shortcuts import HttpResponse, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from app01.models import Host


@login_required(login_url=settings.LOGIN_URL)
def host_list(request):
    """
    主机详情
    :param request:
    :return:
    """
    host_all = Host.objects.all()
    return render(request, 'app01/host_detail.html', {'hosts_info': host_all})
