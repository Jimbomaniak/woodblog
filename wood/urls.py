from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^articles/(?P<article_id>[0-9]+)/$',
        views.single_article, name='single_article'),
    url(r'^about/$', views.about, name='about'),
    url(r'^store', views.store, name='store'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
