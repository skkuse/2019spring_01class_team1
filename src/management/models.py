from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
    pass
    cate = models.CharField(max_length=2,blank=True)
    corporation = models.CharField(verbose_name = 'corporation',max_length=255, blank=True)
    pid = models.CharField(verbose_name = 'pid',max_length=30, blank=True)
    sid = models.CharField(verbose_name = 'sid',max_length=255,blank=True)
    
    def is_md(self):
        if str(self.cate) == 'MD':
            return True
        else:
            return False
    
    def is_rs(self):
        if str(self.cate) == 'RS':
            return True
        else:
            return False

class MD(User):
    # objects = models.Manager()
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=255)
    
    # pid = models.CharField(verbose_name = 'pid',max_length=30, blank=True)
    # cate = models.CharField(verbose_name = 'cate', max_length=2,default="MD")
    # corporation = models.CharField(verbose_name = 'corporation',max_length=255, blank=True)
    # sid = models.CharField(verbose_name = 'sid',max_length=255,blank=True)
    USERNAME_FIELD = 'username'
    # birth_date = models.DateField(null=True, blank=True)
    

    
class RS(User):
    USERNAME_FIELD = 'username'
    # sid = models.CharField(verbose_name = 'sid',max_length=255,blank=True)
    # corporation = models.CharField(verbose_name = 'corporation',max_length=255, blank=True)
    # cate = models.CharField(max_length=2, verbose_name = 'cate', default='RS')


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
        '깔창': 'insole',
        '굽높이': 'heel',
        '앞굽': 'front_heel',
        '총길이': 'shoes_height'
    }
    classes = models.CharField(max_length = 100, default=None, null=True)
    sn = models.AutoField(primary_key=True)
    sid = models.CharField(max_length = 255, null=True, blank=True)
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
    waist = models.CharField(max_length = 100,null=True, blank=True, default=None)
    thigh = models.CharField(max_length = 100,null=True, blank=True, default=None)
    bottom = models.CharField(max_length = 100,null=True, blank=True, default=None)
    crotch = models.CharField(max_length = 100,null=True, blank=True, default=None) # 밑위
    tail = models.CharField(max_length = 100,null=True, blank=True, default=None)
    down_size = models.CharField(max_length = 100,null=True, blank=True, default=None)
    # 신발
    shoes_size = models.FloatField(null=True, blank=True, default=None)
    ball_foot = models.FloatField(null=True, blank=True, default=None) # 발볼
    insole = models.CharField(max_length = 100,null=True, blank=True, default=None) # 깔창
    heel = models.CharField(max_length = 100,null=True, blank=True, default=None) # 굽높이
    front_heel = models.CharField(max_length = 100,null=True, blank=True, default=None) # 앞굽
    shoes_height = models.CharField(max_length = 100,null=True, blank=True, default=None) # 총길이