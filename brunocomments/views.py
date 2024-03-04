from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CommentForm


def new_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CommentForm()
    return render(request, 'form.html', {'form': form})
