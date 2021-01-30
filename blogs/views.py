from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogs.models import Article
from blogs.models import Article
from django.shortcuts import render


def index(request):
    return redirect('home')


def home(request):
    return HttpResponse("Hello World")

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}

    return render(request, 'blogs/article.html', context)
