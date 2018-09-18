from django.contrib import admin
from .models import Post, Product, Maker, PModel, PPhoto, PProduct
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Product)
admin.site.register(Maker)
admin.site.register(PModel)
admin.site.register(PPhoto)
admin.site.register(PProduct)