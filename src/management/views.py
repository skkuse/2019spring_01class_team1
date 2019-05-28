from django.shortcuts import render
from management.functions import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadDocumentForm, UploadFileForm
import os
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


# import django
# import sys
# import torch
# Create your views here.

def html(request):
    
    # print(django.VERSION)
    # print(sys.version)
    # print(torch.__version__)
    return render(request,'html.html')
    
def index(request):
    
    return render(request, 'index.html')
    

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
        # 에러 처리 코드 필요함.
        # 엑셀파일이 아닌 경우, 여러 개 파일이 올라온 경우.
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
    

def login_MD(request):
    
    return render(request, 'ClotheshangerSignup_m.html')

def classify(request):
    
    return None