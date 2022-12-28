from django.shortcuts import render, get_object_or_404,  redirect
from .models import Article
from django.contrib import messages
from .forms import  Contact_Form

# Create your views here.

def index(request):
     posts = Article.objects.all()
     return render(request, "article_list.html", {"object_list": posts})

def detail(request, id):
    article = Article.objects.get(id=str(id))
    return render(request, "article_detail.html", {"article": article})

def create(request):
     if request.method == "POST":
         form = Contact_Form(request.POST)
         if form.is_valid():
             form.save()
             messages.success(request, '登録内容を保存しました。')
     else:
         form = Contact_Form()
     return render(request, "article_form.html", {'form': form})

def update(request, id):
    article = get_object_or_404(Article, id=str(id))
    if request.method == "POST":
         form = Contact_Form(request.POST, instance=article)
         if form.is_valid():
            form.save()
            messages.success(request, '登録内容を変更しました。')
            return render(request, "article_edit.html", {'form': form})
    else:
        form = Contact_Form(instance=article)
        return render(request, "article_edit.html", {'form': form})

def delete(request, id):
    article = get_object_or_404(Article, id=str(id))
    article.delete()
    posts = Article.objects.all()
    return render(request, "article_list.html", {"object_list": posts})
