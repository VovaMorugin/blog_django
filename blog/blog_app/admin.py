from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'rating', 'created', 'updated')
class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'author', 'rating', 'created', 'updated', 'is_active')
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'created', 'updated')
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post')
class SubCommentAdmin(admin.ModelAdmin):
    list_display = ('parent', 'child')
class PostTagAdmin(admin.ModelAdmin):
    list_display = ('post', 'tag')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(SubComment, SubCommentAdmin)
admin.site.register(PostTag, PostTagAdmin)
