from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.http import Http404
from .models import Category, Post

# Create your views here.


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(is_published=True,
                                    pub_date__lte=now(),
                                    category__is_published=True
                                    ).order_by('-pub_date')[:5]

    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'blog/detail.html'
    context = {'post': get_record(pk)}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug)

    if not category.is_published:
        raise Http404('Страница не найдена')

    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=now(),
        category=category.pk
    ).order_by('-pub_date')

    context = {'category': category,
               'post_list': post_list
               }
    return render(request, template_name, context)


def get_record(id):
    post = get_object_or_404(Post, pk=id)
    published = post.is_published
    pub_date_corr = post.pub_date > now()
    cat_published = post.category.is_published
    if not published or pub_date_corr or not cat_published:
        raise Http404('Страница не найдена')

    return post
