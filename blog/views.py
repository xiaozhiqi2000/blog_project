#coding:utf-8

import logging
from django.shortcuts import render
from django.conf import settings  #需要导入这个模块
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger  # 分页器的使用
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
        article_list = Article.objects.all()       #获取所有数据
        paginator = Paginator(article_list,10)     #对取出的数据进行分页,设置10条数据
        try:
            page = int(request.GET.get('page',1))  #获取当前页,如果没有则显示第1页
            article_list = paginator.page(page)    #获取当前页显示的数据
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)
    return render(request,'index.html',locals())   #locals()把当前所有的变量传给前端