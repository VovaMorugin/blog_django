from django import template
from ..models import Category, Post
from datetime import datetime, date

register = template.Library()

@register.inclusion_tag('block_categories.html')
def get_categories():
    categories = Category.objects.all()
    return {
        'categories' : categories
    }

@register.inclusion_tag('last_posts.html')
def get_last_post(max_items=5):
    dt_now = datetime.now()
    filter_date = datetime(dt_now.year, dt_now.month, dt_now.day)
    posts = Post.objects.filter(created__gte=date.today())[:max_items]

    return {
        'posts': posts
    }
