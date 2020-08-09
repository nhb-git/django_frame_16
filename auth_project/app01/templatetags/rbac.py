#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/9/2020  4:30 PM 
# 文件名称   ：rbac.py
from django.conf import settings
from django.template import Library


register = Library()


@register.inclusion_tag('app01/static_menu.html')
def static_menu(request):
    """
    生成菜单
    :param request:
    :return:
    """
    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    current_url = request.path_info
    return {'menu_list': menu_list, 'current_url': current_url}


@register.filter
def has_permission(request, alias):
    """
    判断是否有权限
    :param request:
    :param alias:
    :return:
    """
    if alias in request.session.get(settings.PERMISSION_SESSION_KEY):
        return True
