from django import template
from blog.models import Post
register=template.Library()
from django.db.models import Count

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_posts_123.html')
def show_latest_posts(count=5):
    latest_posts=Post.objects.order_by('-publish')[:count]
    # print(new_posts,"****")
    return {'latest_posts':latest_posts}

#*******Note:**@register.assignment_tag decorator was deprecated in Django 1.9 and removed in Django 2.0. It is recommended to use @register.simple_tag
# @register.assignment_tag
# def get_most_commented_posts(count=5):
#     return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]