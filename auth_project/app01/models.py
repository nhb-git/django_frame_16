from django.db import models
from django.contrib.auth.models import AbstractUser
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

# 项目配置
from auth_project import settings


class User(AbstractUser):
    """自定义用户表"""
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    role = models.ManyToManyField(verbose_name='用户的角色', to='Role', blank=True)

    def generate_confirmation_token(self, expires_in=3600):
        """生成确认Token"""
        s = Serializer(settings.SECRET_KEY, expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def check_activate_token(token):
        """校验token并激活用户"""
        s = Serializer(settings.SECRET_KEY)
        try:
            data = s.loads(token.encode('utf-8'))
        except BadSignature:
            return '无效的激活码'
        except SignatureExpired:
            return '激活码已经过期'
        user = User.objects.filter(id=data.get('id')).first()
        if not user:
            return '激活的账号不存在'
        if not user.is_active:
            user.is_active = True
            user.save()
        return '激活成功'

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Role(models.Model):
    """角色表"""
    name = models.CharField(verbose_name='角色名称', max_length=128, unique=True)
    permission = models.ManyToManyField(verbose_name='角色的权限', to='Permission', blank=True)

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Permission(models.Model):
    """权限表"""
    name = models.CharField(verbose_name='权限名称', max_length=64, unique=True)
    url = models.CharField(verbose_name='权限的url', max_length=256, null=True, blank=True)
    alias = models.CharField(verbose_name='权限别名', max_length=64, null=True, blank=True)
    is_menu = models.BooleanField(verbose_name='是否是菜单', default=False)
    icon = models.CharField(verbose_name='权限图标', max_length=32, blank=True, null=True)
    parent_menu = models.ForeignKey(verbose_name='父菜单', to='self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Host(models.Model):
    """主机表"""
    name = models.CharField(verbose_name='主机名称', max_length=128, unique=True)
    ip = models.GenericIPAddressField(verbose_name='主机IP')
    username = models.CharField(verbose_name='主机账户', max_length=64)
    password = models.CharField(verbose_name='主机密码', max_length=32)
    created_time = models.DateTimeField(verbose_name='主机信息更新时间', auto_now=True)
    owner = models.ForeignKey(verbose_name='主机的拥有者', to='User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '主机'
        verbose_name_plural = verbose_name

    def __str(self):
        return self.name
