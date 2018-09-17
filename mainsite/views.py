from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, Product
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
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
    html = '''
    <!DOCTYPE html>
    <html>
    <head><title>About Myself</title></head>
    <body>
    <h2>Min-Huang Ho</h2>
    <hr>
    <p>
    Hi, I am Min-Huang Ho. Nice to meet you!
    </p>
    </body>
    </html>
    '''
    return HttpResponse(html)