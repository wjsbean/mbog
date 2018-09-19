from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, Product, PProduct, Maker, PPhoto, PModel
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

def sum_a_b(request, a, b):
    template = get_template('Test_url.html')
    html = template.render({'sum_a_b': int(a) + int(b)})
    return HttpResponse(html)

def live_telecast(request, tvno='0'):
    tv_list = [{'name': 'CCTV综合', 'tvcode': 'cctv1'},
               {'name': 'CCTV经济', 'tvcode': 'cctv2'},
               {'name': 'CCTV综艺', 'tvcode': 'cctv3'},
               {'name': 'CCTV国际', 'tvcode': 'cctv4'},
               {'name': 'CCTV体育', 'tvcode': 'cctv5'},
               {'name': 'CCTV电影', 'tvcode': 'cctv6'},
               ]
    tempalate = get_template('live_telecast.html')
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    html = tempalate.render(locals())
    return HttpResponse(html)

def index(request):
    products = PProduct.objects.all()
    template = get_template('index_p.html')
    html = template.render(locals())
    return HttpResponse(html)

def detail_p(request, id):
    try:
        product = PProduct.objects.get(id=id)
        images = PPhoto.objects.filter(product=product)
    except:
        pass
    tempalte = get_template('detail_p.html')
    html = tempalte.render(locals())
    return HttpResponse(html)