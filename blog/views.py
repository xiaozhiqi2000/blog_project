#coding:utf-8

import logging
from django.shortcuts import render
from django.conf import settings  #需要导入这个模块
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger  # 分页器的使用
from blog.models import *
from django.db import connection


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
        paginator = Paginator(article_list,5)     #对取出的数据进行分页,设置10条数据
        try:
            page = int(request.GET.get('page',1))  #获取当前页,如果没有则显示第1页
            article_list = paginator.page(page)    #获取当前页显示的数据
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
        # 文章归档
        # 1.先要器去获取到文章中有的年份-月份
        # 使用values().distinct()是不可行的
        # Article.objects.values('date_publish').distinct() 2016-07
        # 使用原生SQL方法
        # 第1种方式(不可行)
        # archive_list = Article.objects.raw('SELECT DISTINCT DATE_FORMAT(date_publish, "%Y-%m") as col_date FROM blog_article ORDER BY date_publish')
        # for archive in archive_list:
        #    print archive
        # 第2种方式(不推荐)
        # cursor = connection.cursor()
        # cursor.execute('SELECT DISTINCT DATE_FORMAT(date_publish, "%Y-%m") as col_date FROM blog_article ORDER BY date_publish')
        # row = cursor.fetchall()
        # print now
        # 第3种方式，自定义管理器manager
        archive_list = Article.objects.distinct_date()
        # 标签云
        tag_list = Tag.objects.all()
        # 友情链接
        links_list = Links.objects.all()
        # 浏览排行
        click_top_list = Article.objects.all().order_by('-click_count')[:6]
        # 站长推荐
        is_recommend_list = Article.objects.filter(is_recommend=True)[:6]

    except Exception as e:
        logger.error(e)
    return render(request,'index.html',locals())   #locals()把当前所有的变量传给前端


def archive(request):
    try:
        # 分类信息获取(导航数据)
        category_list = Category.objects.all()
        # 广告数据
        ad_list = Ad.objects.all()
        # 文章归档
        archive_list = Article.objects.distinct_date()
        # 先获取客户端提交的信息
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)  # 获取所有数据
        paginator = Paginator(article_list, 5)  # 对取出的数据进行分页,设置10条数据
        try:
            page = int(request.GET.get('page', 1))  # 获取当前页,如果没有则显示第1页
            article_list = paginator.page(page)  # 获取当前页显示的数据
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
        # 标签云
        tag_list = Tag.objects.all()
        # 友情链接
        links_list = Links.objects.all()
    except Exception as e:
        logger.error(e)

    return render(request, 'archive.html', locals())









