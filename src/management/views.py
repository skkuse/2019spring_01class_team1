from management.functions import *
import glob
from django.contrib.auth.decorators import login_required, user_passes_test
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
from .forms import MDCreationForm, MDLoginForm, RSCreationForm, RSLoginForm
from .models import *
import time
import pandas as pd
from functools import wraps

def index(request): 

    return render(request, 'CH_UserSelection.html')

MD_login_required = user_passes_test(lambda u: True if u.is_md() else False, login_url='login_MD')
RS_login_required = user_passes_test(lambda u: True if u.is_rs() else False, login_url='login_RS')
    
def MERCHANDISE_login_required(view_func):
    decorated_view_func = login_required(MD_login_required(view_func), login_url='login_MD')
    return decorated_view_func
    
def RSUSER_login_required(view_func):
    decorated_view_func = login_required(RS_login_required(view_func), login_url='login_RS')
    return decorated_view_func

@login_required
def Logout(request):
    logout(request)
    return redirect(reverse("index"))
    
def login_MD(request): 
    if request.method == 'POST':
        form = MDLoginForm(request.POST)
        
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            print(user.is_authenticated)
            print(user)
            print(MD.objects.all())
            login(request, user)
            print("login success")
            
            return HttpResponseRedirect(reverse('dashboard_MD'))
        else:
            # 로그인창에서 에러메세지 출력
            messages.warning(request,'Fail to log in. Please check id or password')
            # return HttpResponseRedirect(reverse("login_MD"))
            return render(request, 'CH_Login_M.html',{"form":form})
    else:
        form = MDLoginForm()
        
        # return render(request,"CH_Login_M.html")
    
    return render(request, 'CH_Login_M.html',{"form":form})

#@login_required
@MERCHANDISE_login_required
def dashboard_MD(request):
    # print(request.user.cate, request.user.id)
    return render(request, "CH_Dashboard_M.html", {"data":request})
    
#@login_required
@RSUSER_login_required
def dashboard_RS(request):
    # print(request.user.cate)
    return render(request,"CH_Dashboard_R.html", {"data":request})
    
def login_Seller(request):
    if request.method == 'POST':
        form = RSLoginForm(request.POST)
        
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
            messages.warning(request,'Fail to log in. Please check id or password')
            # return HttpResponseRedirect(reverse("login_Seller"))
            return render(request, 'CH_Login_R.html',{"form":form})
    else:
        form = RSLoginForm()
        
    d = RS.objects.all()
    print(d)
    for i in d:
        print(i.username, i.sid, i.cate)
    
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
        print(i.username, i.pid)
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
            
            return HttpResponseRedirect(reverse('login_Seller'))
    else:
        form = RSCreationForm()
        
    d = RS.objects.all()
    print(d)
    for i in d:
        print(i.username, i.sid, i.cate)
    return render(request, 'CH_Signup_R.html',{"form":form})
    

# 엑셀 파일 업르도
# @login_required
@RSUSER_login_required
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
            
            return HttpResponseRedirect(reverse('Pr2'))
    
    
    return render(request, 'CH_FileSubmit_R.html')

# 이미지 업로드
# @login_required
@RSUSER_login_required
def Pr2(request):
    messages.success(request,'엑셀파일이 성공적으로 업로드되었습니다.')
    
    username = "no"
    if request.user.is_authenticated:
        username = request.user
    
    temp = excel_to_data("management/upload/"+str(username))
    result = []
    for dic in temp:
        a = (": ".join(list(dic.items())[0]), ", ".join(['{}: {}'.format(k,v) for k,v in list(dic.items())[1:]]))
        result.append(a)
        
    if request.method=='POST':
        # 매번 지우고 새로 업로드
        if os.path.exists('management/upload/'+str(username)+"/images"):
            shutil.rmtree('management/upload/'+str(username)+"/images")
            
        for file in request.FILES.getlist('file'):
            uploaded_file = file
            # 에러 처리 코드 필요함.
                
            fs=FileSystemStorage(location='management/upload/'+str(username)+"/images")
            fs.save(uploaded_file.name, uploaded_file)
            
        return redirect(reverse("RS_status"))
    
    return render(request, 'CH_ImageSubmit_R.html', {'exceldata':result})

    
#@login_required
@MERCHANDISE_login_required
def Reg_approv(request, name):
    username = request.GET['name']
    
    temp = excel_to_data("management/upload/"+str(username))
    if request.method=='POST':
        filelist = glob.glob("management/upload/"+str(username)+"/*.xlsx")
        df = pd.read_excel(filelist[0], header=1)
        df.columns = [Product.name_dict[i] for i in df.columns]
       
        for idx, i in enumerate(df.itertuples()):
            # print(i)
                # 이미 상품이름이 등록되어 있으면 저장하지 않음.
            n = Product.objects.filter(pname = i.pname)
            if len(n)==0:
                product = Product.objects.create(classes = request.POST[str(idx)], 
                    sid = username, pname = i.pname, material = i.material, color = i.color, measurement = i.measurement,
                    madefrom = i.madefrom, madein = i.madein, date_of_production = i.date_of_production, quality_gurantee = i.quality_gurantee,
                    size = i.size, shoulder = i.shoulder, chest = i.chest, sleeve_len = i.sleeve_len, sleeve_end = i.sleeve_end,
                    armpit = i.armpit, top_size = i.top_size, waist = i.waist, thigh = i.thigh, bottom = i.bottom, crotch = i.crotch,
                    tail = i.tail, down_size = i.down_size, shoes_size = i.shoes_size, ball_foot = i.ball_foot, insole = i.insole, heel = i.heel,
                    front_heel = i.front_heel, shoes_height = i.shoes_height)
            
                print(product)
                product.save()
            # 모델에 저장완료 후, 로컬에 저장된 내용 삭제(엑셀, 이미지)
            
                
        
        shutil.rmtree('management/upload/'+str(username))        
        return redirect(reverse('Reg_status'))
    
    
    result = img_classification("/management/upload/"+str(username))
    
    prod_name = []
    for dic in temp:
        prod_name.append(": ".join(list(dic.items())[0]))
    del temp
    data = [(name, img_route.replace(str(os.getcwd())+"/management","."), classify) for name, (img_route, classify) in zip(prod_name, result)]
    print(data)
        
    return render(request, 'CH_RegistrationApproval_M.html', {"data":data})

# 판매자 리스트 보기.
def Reg_list(request):
    uploaded_list = glob.glob("management/upload/*")
    print(uploaded_list)
    RS_list = [i.split("/")[-1] for i in uploaded_list]
    return render(request, "CH_RegistrationApproval_list.html", {"data":RS_list})

@MERCHANDISE_login_required
def Reg_status(request):
    # 전체 모델값 불러오기
    # print(Product.objects.all())
    products = Product.objects.all()
    context = {'products': products}
    print(products)
    #print(context['products'][0])
    ## 여기 템플릿에서 dashboard 클릭하면 오류뜬다.
    return render(request, "CH_RegistrationStatus_M.html", context)
    
@RSUSER_login_required
def RS_status(request):
    
    # 본인 이름으로 올라온 상품만 봐야 한다
    username = "no"
    if request.user.is_authenticated:
        username = request.user
    # n = Product.objects.filter(username)
    
    try:
    ## 엑셀 파일 올라간거 데이터.
        temp = excel_to_data("management/upload/"+str(username))
        result=[]
        for dic in temp:
            a = list(dic.values())[0] # 상품 이름만 가져오기
            class_ = '대기'
            seller = username
            result.append((a, seller, class_))
        print(result)
    except:
        result=[]
        
    finally:
        products = Product.objects.filter(sid = username)
        return render(request, "CH_RegistrationStatus_R.html", {'products': products, "result" : result})

