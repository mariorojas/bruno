from django.shortcuts import render

from brunocomments.models import Comment


def index(request):
    context = {'comment_list': Comment.objects.order_by('-created_at')}
    return render(request, 'index.html', context)


def new_comment(request):
    return render(request, 'form.html')
