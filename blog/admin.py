#coding:utf-8
from django.contrib import admin
from models import *


# fields\exclude  只显示定义的字段\除掉这些字段
# fieldsets       进行对字段进行分类设置
# list_display    列出可显示的内容
# list_display_links   列出可显示的内容可以进行点击链接
# list_editable   在列表中设置可以编辑的状态
# list_filter
# inlines


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc','click_count',)
    list_display_links = ('title', 'desc',)
    list_editable = ('click_count',)
#
#
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'desc', 'content')
#         }),
#         ('高级设置', {
#             'classes': ('collapse',),
#             'fields': ('click_count', 'is_recommend',)
#         }),
#     )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)

