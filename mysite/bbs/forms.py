
from django import forms
from .models import Article

class Contact_Form(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = Article

        #②表示するモデルクラスのフィールドを定義
        fields = ('id','title','content','author')



