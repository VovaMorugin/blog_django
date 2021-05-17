from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def main_feed(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'feed.html', {
        "categories": categories,
        "posts": page_obj

    })


def filtered_by_category(request, category_code):

    posts = Post.objects.all().filter(category_id=category_code)
    categories = Category.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'feed.html', {
        "posts": page_obj,
        "categories": categories
    })


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'page.html', {
        "post": post
    })
