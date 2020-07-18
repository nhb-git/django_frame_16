from django.db import models
from django.utils import timezone


class Post(models.Model):
    """文章表"""
    title = models.CharField(verbose_name='贴子标题', max_length=200)
    slug = models.CharField(verbose_name='贴子摘要', max_length=200)
    body = models.TextField(verbose_name='贴子内容')
    pub_date = models.DateTimeField(verbose_name='贴子的发表时间', default=timezone.now)

    class Meta:
        # 模型对象返回的结果记录集是按照这个字段反向排序的
        ordering = ('-pub_date',)
        # 定义在admin后台显示的表名称
        verbose_name = '贴子'
        verbose_name_plural = '贴子'

    def __str(self):
        return self.title
