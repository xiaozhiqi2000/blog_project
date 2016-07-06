import logging
from django.shortcuts import render


logger = logging.getLogger('blog.views')

def index(request):
    try:
        file = open('test.txt','r')
    except Exception as e:
        logger.error(e)

    return render(request,'index.html',locals())