from django.contrib import admin
from .models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','category','price','stock')
    list_filter = ['category']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_tag','name','category','price','stock')
    list_filter = ['category']


admin.site.register(Category)
admin.site.register(Book,BookAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
