from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
       
#email = forms.EmailField()
#files = forms.FileField() #파일 업로드
#url = forms.UrlField()
#words = forms.CharField(max_length=200)
#max_number = forms.ChoiceField(choices=[('1','one'), ('2','two')])
