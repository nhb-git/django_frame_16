#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/9/2020  10:25 AM 
# 文件名称   ：init_permission.py
from django.conf import settings


def init_permission(request, user_obj):
    """
    初始化用户权限
    :param request: 请求对象
    :param user_obj: 当前用户对象
    :return:
    """
    permission_queryset = user_obj.role.filter(permission__isnull=False).values(
        'permission__id', 'permission__name', 'permission__url', 'permission__alias',
        'permission__is_menu', 'permission__icon', 'permission__parent_menu',
        'permission__parent_menu__name', 'permission__parent_menu__url').distinct()

    menu_list = list()
    permission_dict = dict()

    for permission_item in permission_queryset:
        permission_dict[permission_item['permission__alias']] = {
            'id': permission_item.get('permission__id'),
            'name': permission_item.get('permission__name'),
            'url': permission_item.get('permission__url'),
            'parent_menu_id': permission_item.get('permission__parent_menu'),
            'parent_menu_name': permission_item.get('permission__parent_menu__name'),
            'parent_menu_url': permission_item.get('permission__parent_menu__url')
        }

        if permission_item.get('permission__is_menu'):
            menu_item_info = {
                'id': permission_item.get('permission__id'),
                'name': permission_item.get('permission__name'),
                'url': permission_item.get('permission__url'),
                'icon': permission_item.get('permission__icon'),
                'parent_menu': permission_item.get('permission__parent_menu')
            }
            menu_list.append(menu_item_info)

    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_list
