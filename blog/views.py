#coding:utf-8

import logging
from django.shortcuts import render
from django.conf import settings  #需要导入这个模块
from blog.models import *

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
    'MEDIA_URL' : settings.MEDIA_URL
    }


def index(request):
    try:
        # 分类信息获取(导航数据)
        category_list = Category.objects.all()
        # 广告数据
        ad_list = Ad.objects.all()
        # 最新文章数据
    except Exception as e:
        logger.error(e)
    result = {'category_list':category_list,'ad_list':ad_list}
    return render(request,'index.html',result)