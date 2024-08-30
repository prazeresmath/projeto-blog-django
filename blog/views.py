from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post

posts = list(range(1000))

PER_PAGE = 9


def index(request):
    posts = (Post.objects.get_published().order_by('-id')) # type: ignore

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def page(request, slug):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
        }
    )


def post(request, slug):
    post = (Post.objects.get_published().filter(slug=slug).first()) # type: ignore

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
        }
    )

def created_by(request, author_pk):
    posts = Post.objects.get_published().filter(created_by__pk=author_pk) # type: ignore

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/created_by.html',
        {
            'page_obj': page_obj,
        }
    )

def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug) # type: ignore

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/category.html',
        {
            'page_obj': page_obj,
        }
    )