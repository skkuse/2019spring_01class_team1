from django.shortcuts import render
from management.functions import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
import os
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


def index(request): 
    return render(request, 'ClotheshangerEnter.html')
def login_MD(request): 
    return render(request, 'Clotheshangerlogin_m.html')
def login_Seller(request):
    return render(request, 'Clotheshangerlogin_s.html')
def signup_MD(request):
    return render(request, 'ClotheshangerSignup_m.html')
def signup_Seller(request):
    return render(request, "ClotheshangerSignup_s.html")
def Ra_m(request):
    return render(request, 'ClotheshangerRa_m.html')
def Rs_m(request):
    return render(request, 'ClotheshangerRs_m.html')

# 엑셀 파일 업르도
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
    
    
    return render(request, 'ClotheshangerPr_s.html')

def gotoPr2(request):
    return redirect(request, "ClotheshangerPr2_s.html")
    
def Pr2(request):
    username = "no"
    if request.user.is_authenticated:
        username = request.user.username
    
    result = excel_to_data("management/upload/"+str(username))
    
    if request.method=='POST':
        for file in request.FILES.getlist('file'):
            uploaded_file = file
            # 에러 처리 코드 필요함.
            fs=FileSystemStorage(location='management/upload/'+str(username)+"/images")
            fs.save(uploaded_file.name, uploaded_file)
            
            # 여기 classification 부분으로 바뀌어야 함
            return render(reqeust, 'ClotheshangerPr2_s.html')
    
    
    return render(request, 'ClotheshangerPr2_s.html', {'exceldata':result})

def Idx_m(request):
    return render(request, 'ClotheshangerIdx_m.html')
def Idx_s(request):
    return render(request, 'ClotheshangerIdx_s.html')

# 엑셀 파일 업로드
def upload(request):
    username = "no"
    if request.user.is_authenticated:
        username = request.user.username
    
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        # print(type(uploaded_file))
        _format = uploaded_file.name.split(".")[-1]
        if _format != 'xlsx' or _format !="xls":
            messages.warning(request,'Uploading the file was failed')
            return render(request, 'upload.html')
            # 오류 메세지 반환
            # return redirect('upload')
        else:
        
            fs = FileSystemStorage(location='management/upload/'+str(username))
            fs.save(uploaded_file.name, uploaded_file)
            messages.success(request,'The file was uploaded successfully')
            return render(request, 'images.html')
        
        #return redirect('images')
        
        
    return render(request, 'upload.html')
    
# 이미지 업로드
def images(request):

    username = "no"
    if request.user.is_authenticated:
        username = request.user.username
    
    result = excel_to_data("management/upload/"+str(username))
    
    if request.method=='POST':
        for file in request.FILES.getlist('file'):
            uploaded_file = file
            # 에러 처리 코드 필요함.
            fs=FileSystemStorage(location='management/upload/'+str(username)+"/images")
            fs.save(uploaded_file.name, uploaded_file)
            
            # 여기 링크 추후에 변경 필요
            return redirect("classification부분")
            
    return render(request, 'images.html',{'exceldata':result})
    



def classify(request):
    
    return None