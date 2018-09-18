"""mbog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from mainsite.views import homepage, showpost, about, listing, sub_listing, sum_a_b
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    re_path('post/(.+)/', showpost),
    path('about/', about),
    path('list/', listing),
    re_path('list/(.+)/', sub_listing),
    re_path('([0-9]+)/([0-9]+)/', sum_a_b),
]
