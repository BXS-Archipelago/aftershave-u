from django.contrib import admin

from .models import Post, Brands, Creators


admin.site.register(Post)
admin.site.register(Brands)
admin.site.register(Creators)