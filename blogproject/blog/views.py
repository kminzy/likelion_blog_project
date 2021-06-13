from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Blog #Blog class import
from django.utils import timezone
from .forms import BlogForm #입력받는 공간
from django.core.paginator import Paginator # Paginator 임포트

# Create your views here.

def home(request): #쿼리셋을 보여주는게 목적인 함수
    #blogs = Blog.objects #Blog 클래스 안의 object를 blogs에 넣는다 => 쿼리셋
    return render(request, 'home.html')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id) #blog_id를 pk로 받는다
    return render(request, 'detail.html', {'details':details})

def postlist(request):
    postlists = Blog.objects.order_by('-pub_date')
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        postlists = Blog.objects.filter(writer=author)
        return render(request, 'postlist.html', {'postlists':postlists})

    # paginator = Paginator(postlists, 3)
    # page = request.GET.get('page')
    # postlists = paginator.get_page(page) #페이지 가져와서 몇 번째 페이지인지 정보 전달
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

# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(username=request.POST['username',], password = request.POST['password1'])
#             auth.login(request, user)
#             return redirect('home')
#     return render(request, 'signup.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username = username, password = password)
#         if user is not None: #실제로 db에 존재하는 유저인지 검증
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': '아이디와 비밀번호가 잘못되었습니다. '})
#     return render(request, 'login.html')

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         redirect('home')
#     return render(request, 'login.html')