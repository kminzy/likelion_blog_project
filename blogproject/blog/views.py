from django.shortcuts import render, get_object_or_404
from .models import Blog #Blog class import

# Create your views here.

def home(request): #쿼리셋을 보여주는게 목적인 함수
    #blogs = Blog.objects #Blog 클래스 안의 object를 blogs에 넣는다 => 쿼리셋
    return render(request, 'home.html')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id) #blog_id를 pk로 받는다
    return render(request, 'detail.html', {'details':details})

def postlist(request):
    postlists = Blog.objects
    return render(request, 'postlist.html', {'postlists':postlists})

def about(request):
    return render(request, 'about.html')