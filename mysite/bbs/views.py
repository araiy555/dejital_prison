from django.shortcuts import render, get_object_or_404,  redirect
from .models import Article
from django.contrib import messages
from .forms import  Contact_Form
from .forms import  CommentCreateForm
from .forms import  SearchForm
from .models import Comment
from django.core.paginator import Paginator

# Create your views here.
def index(request):
     posts = Article.objects.all()
     search_form = SearchForm()

     paginator = Paginator(posts, 10) # 1ページに10件表示
     p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
     articles = paginator.get_page(p) # 指定のページのArticleを取得
     return render(request, "article_list.html", {"object_list": articles, "search_form": search_form,})

def detail(request, id):
    article = Article.objects.get(id=str(id))

    try:
        comment_list = Comment.objects.filter(target=id)
        form = CommentCreateForm()

    except Comment.DoesNotExist:
        comment_list = None
        form = CommentCreateForm()

    return render(request, "article_detail.html", {"article": article, 'form': form , "comment": comment_list })

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

def comment(request, id):
    form = CommentCreateForm(request.POST)
    if form.is_valid():
        article = get_object_or_404(Article, id=str(id))
        comment = form.save(commit=False)
        comment.target = article
        comment.save()

        try:
            comment_list = Comment.objects.filter(target=id)
            form = CommentCreateForm()

        except Comment.DoesNotExist:
            comment_list = None
            form = CommentCreateForm()

        return render(request, "article_detail.html", {"article": article, 'form': form , "comment": comment_list })


def search(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword'] # keyword変数にフォームのキーワードを代入
        articles = Article.objects.filter(title__contains=keyword) # キーワードを含むレコードをfilterメソッドで取り出し、articles変数に代入
    else:
        searchform = SearchForm() # searchForm変数をSearchFormオブジェクトで上書き
        articles = Article.objects.all() # すべてのレコードを取得

    return render(request, 'article_search.html',  {"article": articles, "search_form":searchForm })

