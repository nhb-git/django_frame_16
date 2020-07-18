from django.contrib import admin

from mainsite.models import Post


class PostAdmin(admin.ModelAdmin):
    """Post模型在admin后台的自定义显示列"""
    list_display = ('title', 'slug', 'pub_date')


admin.site.register(Post, PostAdmin)
