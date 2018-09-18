from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    
    #class Meta:
    #    ordering = ('-pub_date')
        
    def __str__(self):
        return self.title

class Product(models.Model):
    Sizes = (
        ('S', 'Smail'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    #sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    qty = models.CharField(max_length=2, default='0')

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')

    def __str__(self):
        return self.name


class PProduct(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, default="二手手机")
    description = models.TextField(default="暂无说明")
    year = models.PositiveIntegerField(default=2016)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname


class PPhoto(models.Model):
    product = models.ForeignKey(PProduct, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default="产品照片")
    url = models.URLField(default="http://i.imgur.com/z230eeq.png")

    def __str__(self):
        return self.description