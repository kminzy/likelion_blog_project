from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta: #Blog 모델에 fields 연결, 일종의 이름표 역할, 이 정보를 가지고 BlogForm을 만들어 주겠다
        model = Blog
        fields = ['title','writer','body','image']