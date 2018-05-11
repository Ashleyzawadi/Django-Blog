from django.shortcuts import render
# from django.conf.urls import url 
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html', {'articles':articles})      #return posts.html which is in arcades folder

def article_detail(request, slug):
    article=Article.objects.get(slug=slug)
    return HttpResponse(slug)