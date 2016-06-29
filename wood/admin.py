from django.contrib import admin
from .models import Article, Product, Category, Comments

admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(Product)
admin.site.register(Category)
