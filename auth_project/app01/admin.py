from django.contrib import admin

# 用户模型
from app01.models import User, Role, Permission, Host

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)


class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'created_time', 'owner')


admin.site.register(Host, HostAdmin)
