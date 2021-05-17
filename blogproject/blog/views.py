from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog #Blog class import
from django.utils import timezone
from .forms import BlogForm #입력받는 공간

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
    form = BlogForm() #선언
    return render(request, 'new.html', {'form':form}) #객체 리턴

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid(): #폼이 유효한지 체크
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('/blog/' + str(new_blog.id))
    return redirect('home') #등록 실패하면 홈으로

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