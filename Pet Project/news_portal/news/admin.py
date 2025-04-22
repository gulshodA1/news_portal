from django.contrib import admin

from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    list_filter = ('created_date',)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)