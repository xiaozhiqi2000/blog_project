#coding:utf-8

import logging
from django.shortcuts import render
#使用settings全局变量需要导入这个模块
from django.conf import settings
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger  # 分页器的使用
from blog.models import *
# from django.db import connection
from django.db.models import Count

logger = logging.getLogger('blog.views')

# 通过定义一个方法来返回全局配置中的变量,setting在templates需要设置这个方法,在前端使用key，例如{{SITE_NAME}}来调用

def global_setting(request):

    # 重构一：将分类，广告，文章归档，标签云，友情链接，浏览排序行，站长推荐，评论排行等这些公共数据放入全局
    # 分类信息获取(导航数据)
    category_list = Category.objects.all()
    # 广告数据
    ad_list = Ad.objects.all()
    # 文章归档
    archive_list = Article.objects.distinct_date()
    # 标签云
    tag_list = Tag.objects.all()
    # 友情链接
    links_list = Links.objects.all()
    # 浏览排行
    click_top_list = Article.objects.all().order_by('-click_count')[:6]
    # 评论排行
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('comment_count')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
    # 站长推荐
    is_recommend_list = Article.objects.filter(is_recommend=True)[:6]

    return {
    'SITE_NAME' : settings.SITE_NAME,
    'SITE_DESC' : settings.SITE_DESC,
    'WEIBO_SINA' : settings.WEIBO_SINA,
    'WEIBO_TENCENT' : settings.WEIBO_TENCENT,
    'PRO_RSS' : settings.PRO_RSS,
    'PRO_EMAIL' : settings.PRO_EMAIL,
    'MEDIA_URL' : settings.MEDIA_URL,
    'category_list' : category_list,
    'ad_list' : ad_list,
    'archive_list' : archive_list,
    'tag_list' : tag_list,
    'links_list' : links_list,
    'click_top_list' : click_top_list,
    'is_recommend_list' : is_recommend_list,
    'article_comment_list' : article_comment_list
    }


def index(request):
    try:
        article_list = getPage(request,Article.objects.all())
    except Exception as e:
        print e
        logger.error(e)
    return render(request,'index.html',locals())


def archive(request):
    try:
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)

        article_list = getPage(request,article_list)
    except Exception as e:
        logger.error(e)
    return render(request, 'archive.html', locals())

# 重构三：对分页代码的重构
def getPage(request,article_list):
    paginator = Paginator(article_list, 5)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list




