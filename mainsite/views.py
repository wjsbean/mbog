from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, Product
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
import random
# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    post_lists = list()
    now = datetime.now()
    html = template.render(locals())
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<hr>")
        post_lists.append("<small>" + str(post.body) + "</small><br><br>")

    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    #html = template.render(locals())
    #return HttpResponse('fef'+slug)
    try:
    #    return HttpResponse("A test: " + slug)
        post = Post.objects.get(slug=slug)
        #post = posts.get(slug=slug)
        if post is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def listing(request):
    template = get_template('listing.html')
    try:
        products = Product.objects.all()
        if products is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def sub_listing(request, name):
    template = get_template('sub_listing.html')
    try:
        product = Product.objects.get(name=name)
        if product is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except Product.DoesNotExist:
        raise Http404('找不到你要查询的产品，请核对后重新输入')

def about (request):
    template = get_template('about.html')
    quotes = [
        '今日事，今日毕',
        '要收获，先付出',
        '知识就是力量',
        '一个人的个性就是他的命运'
    ]
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)