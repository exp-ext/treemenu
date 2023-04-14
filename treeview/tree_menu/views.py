from django.shortcuts import render
from django.views.generic import TemplateView


class PageView(TemplateView):
    template_name = 'base.html'


def post_detail(request, post_id):

    post = f'Пост номер {post_id}'
    context = {
        'post': post,
    }
    template = 'posts/post_detail.html'
    return render(request, template, context)
