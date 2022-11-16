from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps
from django.contrib import admin
from django.urls import path, include

from aftershave_u.views import index, about, robots_txt

from .sitemaps import BrandsSitemap, PostSitemap

sitemaps = {'brands': BrandsSitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('blog.urls')),
    path('', index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
