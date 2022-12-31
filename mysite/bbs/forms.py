
from django import forms
from .models import Article
from .models import Comment


class Contact_Form(forms.ModelForm):
    """記事投稿フォーム"""
    class Meta():
        #①モデルクラスを指定
        model = Article

        #②表示するモデルクラスのフィールドを定義
        fields = ('id','title','content','author')

class CommentCreateForm(forms.ModelForm):
    """コメントフォーム"""
    class Meta:
        model = Comment
        exclude = ('target', 'created_at')

class SearchForm(forms.Form):
        keyword = forms.CharField(label='', max_length=50)
