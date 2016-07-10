from django.shortcuts import render, render_to_response, redirect
from .models import Article, Product, Comment, Category
from .forms import CommentForm, PurchaseForm
from django.template.context_processors import csrf


def main(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'wood/main.html', context)


def single_article(request, article_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    return render_to_response('wood/article.html', args)


def add_comment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
    return redirect('/articles/get/%s' % article_id)


def store(request):
    get_products = Product.objects.all()
    get_categories = Category.objects.all()
    content = {'products': get_products, 'categories': get_categories}
    return render(request, 'wood/store.html', content)


def store_item(request, product_id):
    get_product = Product.objects.get(id=product_id)
    purchase_form = PurchaseForm
    content = {'product': get_product, 'form': purchase_form}
    return render(request, 'wood/store_item.html', content)


def store_category(request, category_id):
    category = Category.objects.get(id=category_id)
    get_by_category = Product.objects.filter(category=category_id)
    content = {'products': get_by_category, 'category': category}
    return render(request, 'wood/store_category.html', content)


def store_purchase(request, product_id):
    if request.POST:
        purchase_form = PurchaseForm(request.POST)
        if purchase_form.is_valid():
            form = purchase_form.save(commit=False)
            form.product = Product.objects.get(id=product_id)
            form.save()
    return redirect('store_item', product_id=product_id)


def about(request):
    return render(request, 'wood/about.html')
