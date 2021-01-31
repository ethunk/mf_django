from django.contrib import admin

from .models import Comment, Article, StockTicker, Author

@admin.register(Article)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'headline', 'publish_at')
    list_filter = ('author',)
    search_fields = ('author', 'body', 'headline')

@admin.register(Author)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name', 'email')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'article', 'created', 'active')
    search_fields = ('name', 'article', 'body')
