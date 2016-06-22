from django.shortcuts import render, get_object_or_404
from .models import Article, Product


def main(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'wood/main.html', context)


def single_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'wood/article.html', {'article': article})


def store(request):
    get_products = Product.objects.all()
    products = {'products': get_products}
    return render(request, 'wood/store.html', products)


def about(request):
    return render(request, 'wood/about.html')
