from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def main_feed(request):
    posts = Post.objects.all()
    category_id = int(request.GET.get('category', 0))

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'feed.html', {
        "posts": page_obj,
        "category_id": category_id

    })


def filtered_by_category(request, category_code):
    posts = Post.objects.all().filter(category_id=category_code)
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'feed.html', {
        "posts": page_obj
    })


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'page.html', {
        "post": post
    })
