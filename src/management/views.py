from django.shortcuts import render
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