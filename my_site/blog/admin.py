from django.contrib import admin
from .models import Tag, Author, Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Date', 'author',)
  list_filter = ('author', 'Date', 'tags',)
  prepopulated_fields = {"Slug": ('Title',)}


class CommentAdmin(admin.ModelAdmin):
  list_display = ('user_name', 'user_email', 'post',)
  list_filter = ('id', 'user_name', 'user_email', 'post',)

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
