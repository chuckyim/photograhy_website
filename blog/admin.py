from django.contrib import admin
from .models import Blog, BlogImage

# admin.site.register(Blog)  <--this line is original from Nick's tutorial

class BlogImageAdmin(admin.StackedInline):
    model = BlogImage

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageAdmin]

    class Meta:
       model = Blog

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    pass
