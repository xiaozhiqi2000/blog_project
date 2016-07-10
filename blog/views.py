#coding:utf-8

import logging
from django.shortcuts import render
from django.conf import settings  #需要导入这个模块
from blog.models import Category

logger = logging.getLogger('blog.views')

#通过定义一个方法来返回全局配置中的变量
#setting在templates需要设置这个方法
#在前端使用key，例如{{SITE_NAME}}来调用
def global_setting(request):
    return {
    'SITE_NAME' : settings.SITE_NAME,
    'SITE_DESC' : settings.SITE_DESC,
    'WEIBO_SINA' : settings.WEIBO_SINA,
    'WEIBO_TENCENT' : settings.WEIBO_TENCENT,
    'PRO_RSS' : settings.PRO_RSS,
    'PRO_EMAIL' : settings.PRO_EMAIL,
    }


def index(request):
    try:
        category_list = Category.objects.all()
    except Exception as e:
        logger.error(e)

    return render(request,'index.html',{'category_list':category_list})