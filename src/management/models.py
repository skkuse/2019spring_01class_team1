from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class MD(AbstractUser):
    # objects = models.Manager()
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=255)
    pid = models.CharField(verbose_name = 'pid',max_length=30, blank=True)
    cate = models.CharField(max_length=2,default=None)
    corp = models.CharField(max_length=255, default=None, blank=True)
    sid = models.CharField(verbose_name = 'sid',max_length=255,default=None)
    USERNAME_FIELD = 'username'
    # birth_date = models.DateField(null=True, blank=True)
    


    
class Seller(models.Model):
    sid = models.AutoField(primary_key=True)
    # password
    name = models.CharField(max_length=20)
    pid = models.ForeignKey(MD, on_delete = models.SET_NULL, null=True)

class Product(models.Model):
    name_dict = {
        '상품id':'sn',
        'ForeignKey':'sid',
        '제품이름': 'pname',
        '소재': 'material',
        '색상':'color',
        '치수': 'measurement',
        '제조자(수입국)':'madefrom',
        '제조국':'madein',
        '제조연월':'date_of_production',
        '품질보증기간':'quality_gurantee',
        
        '사이즈':'size',
        '어깨':'shoulder',
        '가슴(밑위)':'chest',
        '소매길이': 'sleeve_len',
        '소매끝단면': 'sleeve_end' ,
        '겨드랑이단면': 'armpit',
        '총장': 'top_size',
        '허리단면': 'waist',
        '허벅지단면': 'thigh',
        '엉덩이단면': 'bottom',
        '밑위': 'crotch',
        '밑단면': 'tail',
        '기장': 'down_size',
        '사이즈(cm)': 'shoes_size',
        '발볼': 'ball_foot',
        '깔창': 'heel',
        '굽높이': 'front_heel',
        '앞굽': 'front_heel',
        '총길이': 'shoes_height'
    }
    classes = models.CharField(max_length = 100, default=None, null=True)
    sn = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Seller, on_delete = models.CASCADE)
    pname = models.CharField(max_length=255)
    material = models.CharField(max_length = 255)
    color = models.CharField(max_length=100)
    measurement = models.CharField(max_length=100,null=True, blank=True, default=None)
    madefrom = models.CharField(max_length = 100, default=None)
    madein = models.CharField(max_length=100, default=None)
    date_of_production = models.CharField(max_length=100,null=True, blank=True, default=None)
    quality_gurantee = models.CharField(max_length=100,null=True, blank=True, default=None)
    # 상의
    size = models.CharField(max_length=100,null=True, blank=True, default=None)
    shoulder = models.CharField(max_length=100,null=True, blank=True, default=None)
    chest = models.CharField(max_length=100,null=True,blank=True, default=None)
    sleeve_len = models.CharField(max_length=100,null=True, blank=True, default=None)
    sleeve_end = models.CharField(max_length=100,null=True, blank=True, default=None)
    armpit = models.CharField(max_length=100,null=True, blank=True, default=None)
    top_size = models.CharField(max_length=100,null=True, blank=True, default=None)
    # 하의
    waist = models.FloatField(null=True, blank=True, default=None)
    thigh = models.FloatField(null=True, blank=True, default=None)
    bottom = models.FloatField(null=True, blank=True, default=None)
    crotch = models.FloatField(null=True, blank=True, default=None) # 밑위
    tail = models.FloatField(null=True, blank=True, default=None)
    down_size = models.FloatField(null=True, blank=True, default=None)
    # 신발
    shoes_size = models.IntegerField(null=True, blank=True, default=None)
    ball_foot = models.IntegerField(null=True, blank=True, default=None) # 발볼
    insole = models.FloatField(null=True, blank=True, default=None) # 깔창
    heel = models.FloatField(null=True, blank=True, default=None) # 굽높이
    front_heel = models.FloatField(null=True, blank=True, default=None) # 앞굽
    shoes_height = models.FloatField(null=True, blank=True, default=None) # 총길이