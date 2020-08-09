from django.db import models


class User(models.Model):
    """用户表"""
    name = models.CharField(verbose_name='用户名', max_length=20, null=False)
    email = models.EmailField(verbose_name='邮箱')
    password = models.CharField(verbose_name='密码', max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
