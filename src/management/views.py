from management.functions import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import shutil
from .forms import MDCreationForm, MDLoginForm, RSCreationForm
from .models import *
import time

def index(request): 
    # sd = User.objects.get(username='test1')
    # print(sd.cate)
    # t = User.objects.all()
    # for i in t:
    #     print(t)
    # print(request.user.id)
    
    # 맨 뒷부분 no는 나중에 바꿔줘야 함.
    # r = img_classification("/src/management/upload/no")
    # print(r)
    return render(request, 'CH_UserSelection.html')

@login_required
def Logout(request):
    logout(request)
    return redirect(reverse("index"))
    
def login_MD(request): 
    print(request.user.cate)
    
    # d = MD.objects.all()
    # print(d)
    # for i in d:
    #     print(i.username, i.pid)
    if request.method == 'POST':
        form = MDLoginForm(request.POST)
        
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            print(user.is_authenticated)
            print(user)
            login(request, user)
            print("login success")
            return HttpResponseRedirect(reverse('dashboard_MD'))
        else:
            # 로그인창에서 에러메세지 출력
            return HttpResponseRedirect(reverse("login_MD"))
    else:
        form = MDLoginForm()
        # return render(request,"CH_Login_M.html")
    
    return render(request, 'CH_Login_M.html',{"form":form})

# @login_required
def dashboard_MD(request):
    # print(request.user.cate, request.user.id)
    return render(request, "CH_Dashboard_M.html", {"data":request})
    
# @login_required
def dashboard_RS(request):
    # print(request.user.cate)
    return render(request,"CH_Dashboard_R.html", {"data":request})
    
def login_Seller(request):
    if request.method == 'POST':
        form = MDLoginForm(request.POST)
        
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            print(user.is_authenticated)
            print(user)
            login(request, user)
            print("login success")
            return HttpResponseRedirect(reverse('dashboard_RS'))
        else:
            # 로그인창에서 에러메세지 출력
            return HttpResponseRedirect(reverse("login_Seller"))
    else:
        form = MDLoginForm()

    
    return render(request, 'CH_Login_R.html',{"form":form})

    
def signup_MD(request):
    if request.method == 'POST':
        form = MDCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.pid = form.cleaned_data.get('pid')
            user.cate = "MD"
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(user, user.username, user.pid)
            
            user = authenticate(username=username, password=raw_password)

            # 회원가입 완료 안내 팝업창 필요
            
            return HttpResponseRedirect(reverse('login_MD'))
    else:
        form = MDCreationForm()
        
    d = MD.objects.all()
    print(d)
    for i in d:
        print(i.username, i.pid, i.cate)
    return render(request, 'CH_Signup_M.html',{"form":form})
    
def signup_Seller(request):
    if request.method == 'POST':
        form = RSCreationForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.corporation = form.cleaned_data.get('corporation')
            user.cate = "RS"
            # print(user.cate)
            user.sid = str(time.time())
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            print(user, user.username, user.corporation)
            
            user = authenticate(username=username, password=raw_password)

            # 회원가입 완료 안내 팝업창 필요
            
            return HttpResponseRedirect(reverse('Login_Seller'))
    else:
        form = RSCreationForm()
        
    d = RS.objects.all()
    print(d)
    for i in d:
        print(i.username, i.sid, i.cate)
    return render(request, 'CH_Signup_R.html',{"form":form})
    
def Ra_m(request):
    return render(request, 'ClotheshangerRa_m.html')
def Rs_m(request):
    return render(request, 'ClotheshangerRs_m.html')

# 엑셀 파일 업르도
# @login_required
def Pr(request):
    
    username = "no"
    if request.user.is_authenticated:
        username = request.user.username
    
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        _format = uploaded_file.name.split(".")[-1]
        if (_format != 'xlsx') and (_format !="xls"):
            messages.warning(request,'업로드한 파일 형식이 올바르지 않습니다. 엑셀 파일이 맞는지 확인해 주세요.')
            return render(request, 'ClotheshangerPr_s.html')
        else:
            
            fs = FileSystemStorage(location='management/upload/'+str(username))
            dir_ = glob.glob("management/upload/"+str(username)+"/*.*")
            # 이미 업로드된 파일이 있으면 지운다
            if len(dir_)==1:
                os.remove(dir_[0])
            fs.save(uploaded_file.name, uploaded_file)
            
            # 여기 안 나옴. 수정 필요.
            messages.success(request,'엑셀파일이 성공적으로 업로드되었습니다.')
            
            return HttpResponseRedirect(reverse('Pr2'))
    
    
    return render(request, 'CH_FileSubmit_R.html')

# 이미지 업로드
# @login_required
def Pr2(request):
    username = "no"
    if request.user.is_authenticated:
        username = request.user
    
    temp = excel_to_data("management/upload/"+str(username))
    result = []
    for dic in temp:
        a = (": ".join(list(dic.items())[0]), ", ".join(['{}: {}'.format(k,v) for k,v in list(dic.items())[1:]]))
        result.append(a)
        
    if request.method=='POST':
        for file in request.FILES.getlist('file'):
            uploaded_file = file
            # 에러 처리 코드 필요함.
            # 매번 지우고 새로 업로드
            if os.path.exists('management/upload/'+str(username)+"/images"):
                shutil.rmtree('management/upload/'+str(username)+"/images")
                
            fs=FileSystemStorage(location='management/upload/'+str(username)+"/images")
            fs.save(uploaded_file.name, uploaded_file)
            
            # 여기 classification 담당하는 부분으로 바꿔야 함
            # return render(request, 'ClotheshangerPr2_s.html')
    
    
    return render(request, 'CH_ImageSubmit_R.html', {'exceldata':result})

def Idx_m(request):
    return render(request, 'ClotheshangerIdx_m.html')
def Idx_s(request):
    return render(request, 'ClotheshangerIdx_s.html')
    
#@login_required
def Reg_approv(request):
    username = "no"
    if request.user.is_authenticated:
        username = request.user
    result = img_classification("/src/management/upload/"+str(username))
    temp = excel_to_data("management/upload/"+str(username))
    prod_name = []
    for dic in temp:
        prod_name.append(": ".join(list(dic.items())[0]))
    del temp
    data = [(name, img_route, classify) for name, (img_route, classify) in zip(prod_name, result)]
    return render(request, 'CH_RegistrationApproval_M.html', {"data":data})

def Reg_status(request):
    
    ## 여기 템플릿에서 dashboard 클릭하면 오류뜬다.
    return render(request, "CH_RegistrationStatus_M.html")
