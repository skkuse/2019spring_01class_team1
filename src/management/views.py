from django.shortcuts import render
from management.functions import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadDocumentForm, UploadFileForm
import os
from django.core.files.storage import FileSystemStorage

import pandas as pd

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
        # print(uploaded_file.name)
        fs = FileSystemStorage(location='management/upload/'+str(username))
        fs.save(uploaded_file.name, uploaded_file)
        #asfdfg
        
    return render(request, 'upload.html')
    
# 이미지 업로드
def images(request):
    
    
    
    username = "no"
    if request.user.is_authenticated:
        username = request.user.username
    
    result = excel_to_data("management/upload/"+str(username))
    # file path만 되어 있고 엑셀파일을 구체적으로 짚지 못했다. 그거만 해결하면됨.
    
    if request.method=='POST':
        for file in request.FILES.getlist('file'):
            uploaded_file = file
            fs=FileSystemStorage(location='management/upload/'+str(username))
            fs.save(uploaded_file.name, uploaded_file)
            
    return render(request, 'images.html',{'exceldata':result})