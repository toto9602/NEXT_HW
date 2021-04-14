from django.shortcuts import render, redirect
from .models import Article
import time 

# Create your views here.

def index(request):
    movie_count = Article.objects.filter(category="movie").count()
    drama_count = Article.objects.filter(category="drama").count()
    programming_count = Article.objects.filter(category="programming").count()
    return render(request, 'index.html', {'movie_count':movie_count, 'drama_count':drama_count, 'programming_count':programming_count})

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article':article})

def new(request):
    if request.method == 'POST' :
        print(request.POST) #data 확인
        new_article = Article.objects.create(
            title = request.POST['title'],
            article = request.POST['article'],
            category = request.POST['category']
        )
        return redirect('detail', article_pk=new_article.pk)

    #POST 요청이 아닐 경우
    return render(request, 'new.html')

def movie(request):
    movies = Article.objects.filter(category="movie")
    return render(request, 'movie.html', {'articles': movies})

def drama(request):
    dramas = Article.objects.filter(category="drama")
    return render(request, 'movie.html', {'articles':dramas})

def programming(request):
    programmings = Article.objects.filter(category="programming")
    return render(request, 'programming.html', {'articles': programmings})


