from django.contrib import admin
from blog.models import Post,Comment

# Register your models here Post.======================================

class PostAdmin(admin.ModelAdmin):
    # list_display=['title','slug','author','body','publish','created','updated','status']
    list_display=['title','author','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','author','created','publish')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']

admin.site.register(Post,PostAdmin)

# Register your models here Comment.=================================

class CommentAdmin(admin.ModelAdmin):
    # list_display=('name','email','post','body','created','updated','active')
    #  Remove body (its taking too much space.)
    list_display=('name','email','post','created','updated','active')
    list_filter=('active','post','created','updated')
    search_fields=('name','email','body')

admin.site.register(Comment,CommentAdmin)    