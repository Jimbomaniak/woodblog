from django.contrib import admin
from .models import Article, Product, Category, Comment, Purchase

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Purchase)