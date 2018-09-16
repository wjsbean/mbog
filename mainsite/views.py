from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
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