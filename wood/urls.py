from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^articles/get/(?P<article_id>[0-9]+)/$', views.single_article, name='single_article'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.add_comment),
    url(r'^about/$', views.about, name='about'),
    url(r'^store/$', views.store, name='store'),
    url(r'^store/(?P<product_id>[0-9]+)/$', views.store_item, name='store_item'),
    url(r'^store/category/(?P<category_id>[0-9]+)/$', views.store_category, name='store_category')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
