from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Post


def article_list(request):
    qs = Post.objects.filter(status='published').order_by('-created_at')

    paginator = Paginator(qs, 9)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    return render(request, 'blog/article_list.html', {
        'articles': articles
    })


def article_detail(request, slug):
    article = get_object_or_404(
        Post,
        slug=slug,
        status='published'
    )

    content = article.content.replace('sandbox', '')

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'content': content
    })
