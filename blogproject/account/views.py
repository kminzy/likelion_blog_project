from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
# Create your views here.

def login_view(request): #그냥 login으로 쓰면 auth에서 가져오는 login과 충돌
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username") #유효성 검사 통과한 클린한 데이터의 username가져와서 변수에 저장
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password) #값들 authenticate에 넣고 인증 받음, 객체 생성
            if user is not None: #유저가 존재할 때 로그인
                login(request, user)
        return redirect("home")
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == 'POST': #request method가 post면 form을 받음
        form = RegisterForm(request.POST)
        if form.is_valid(): #폼 받은 후 유효성 검사
            user = form.save() #폼을 저장, 폼 안에 적어주는 정보 외에 필요한 정보 없음, commit 작성x
            login(request, user)
        return redirect("home")
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form':form})