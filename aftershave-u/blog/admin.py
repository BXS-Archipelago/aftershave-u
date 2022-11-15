from django.contrib import admin

from .models import Post, Brands


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'brands', 'created_at']
    list_filter = ['brands', 'created_at']
    prepopulated_fields = {'slug': ('title',)}


class BrandsAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Brands, BrandsAdmin)
