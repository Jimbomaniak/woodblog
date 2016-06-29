from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .models import Article, Product, Comments
from .forms import CommentForm
from django.core.context_processors import csrf



def main(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'wood/main.html', context)


def single_article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    return render_to_response('wood/article.html', args)


def store(request):
    get_products = Product.objects.all()
    products = {'products': get_products}
    return render(request, 'wood/store.html', products)


def about(request):
    return render(request, 'wood/about.html')

def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article =Article.objects.get(id=article_id)
            form.save()
    return redirect('/articles/get/%s' % article_id)
