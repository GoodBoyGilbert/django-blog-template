from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

# Create your views here.

def index(request, category_slug=None):
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = BlogPost.objects.filter(categories=category)
    else:
        category = None
        posts = BlogPost.objects.all()

    posts = posts.order_by('pub_date')

    # Define the number of posts per page
    posts_per_page = 12
    paginator = Paginator(posts, posts_per_page)

    page = request.GET.get('page')
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results.
        paginated_posts = paginator.page(paginator.num_pages)

    recommended_posts = random.sample(list(BlogPost.objects.all()), min(5, BlogPost.objects.count()))

    return render(request, "index.html", {
        'categories': categories,
        'category': category,
        'posts': paginated_posts,
        'recommended_posts': recommended_posts,
    })


def quotepost(request, post_id, category_slug=None):
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = BlogPost.objects.filter(categories=category)
    else:
        category = None
        posts = BlogPost.objects.all()
    
    posts = posts.order_by('pub_date')
    recommended_posts = random.sample(list(BlogPost.objects.all()), min(5, BlogPost.objects.count()))
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "quotepost.html", {'post': post, 'categories': categories, 'category': category, 'posts': posts, 'recommended_posts': recommended_posts})


def category_posts(request, category_slug):
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = BlogPost.objects.filter(categories=category)
    else:
        category = None
        posts = BlogPost.objects.all()

    posts = posts.order_by('pub_date')

    # Define the number of posts per page
    posts_per_page = 12
    paginator = Paginator(posts, posts_per_page)

    page = request.GET.get('page')
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results.
        paginated_posts = paginator.page(paginator.num_pages)

    recommended_posts = random.sample(list(BlogPost.objects.all()), min(5, BlogPost.objects.count()))

    return render(request, 'category_posts.html', {
        'category': category,
        'posts': paginated_posts,
        'categories': categories,
        'paginated_posts': paginated_posts,
        'recommended_posts': recommended_posts,
    })

def about(request, category_slug=None):
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = BlogPost.objects.filter(categories=category)
    else:
        category = None
        posts = BlogPost.objects.all()
    
    posts = posts.order_by('pub_date')
    recommended_posts = random.sample(list(BlogPost.objects.all()), min(5, BlogPost.objects.count()))
    return render(request, "about.html", {'categories': categories, 'category': category, 'posts': posts, 'recommended_posts': recommended_posts})