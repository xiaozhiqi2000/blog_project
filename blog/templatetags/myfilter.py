#/usr/bin/env python
#coding:utf8

from django import template
register = template.Library()

# 定义一个将日期中的月份转换为大写的过滤器,如8转换成八
#@register.filter
def month_to_upper(key):
    return ['一','二','三','四','五','六','七','八','九','十','十一','十二'][key.month-1]


# 注册过滤器,如果使用上面的装饰器则不需要下面这句
# (前)注册名和(后)函数名一样好记,不一样也可以则前端调用的是注册名
register.filter('month_to_upper',month_to_upper)