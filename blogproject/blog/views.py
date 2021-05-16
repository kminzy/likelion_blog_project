from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog #Blog class import
from django.utils import timezone

# Create your views here.

def home(request): #쿼리셋을 보여주는게 목적인 함수
    #blogs = Blog.objects #Blog 클래스 안의 object를 blogs에 넣는다 => 쿼리셋
    return render(request, 'home.html')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id) #blog_id를 pk로 받는다
    return render(request, 'detail.html', {'details':details})

def postlist(request):
    postlists = Blog.objects.all()
    return render(request, 'postlist.html', {'postlists':postlists})

def about(request):
    return render(request, 'about.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST.get('title', False)
    blog.body = request.POST.get('body', False)
    blog.writer = request.POST.get('writer', False)
    blog.pub_date = timezone.datetime.now()
    blog.image = request.FILES.get('image', False)
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST.get('title', False)
    update_blog.body = request.POST.get('body', False)
    update_blog.writer = request.POST.get('writer', False)
    update_blog.pub_date = timezone.datetime.now()
    update_blog.save()
    return redirect('/blog/' + str(update_blog.id))

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('postlist')