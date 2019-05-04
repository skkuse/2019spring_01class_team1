from django.db import models

# Create your models here.
class MD(models.Model):
    pid = models.AutoField(primary_key=True)
    # 패스워드는 장고에서 어떻게 처리하는지 확인해야 한다. password = 
    name = models.CharField(max_length=20)
    
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
    
    sn = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Seller, on_delete = models.CASCADE)
    pname = models.CharField(max_length=255)
    material = models.CharField(max_length = 255)
    color = models.CharField(max_length=100)
    measurement = models.FloatField(null=True, blank=True, default=None)
    madefrom = models.CharField(max_length = 100, default=None)
    madein = models.CharField(max_length=100, default=None)
    date_of_production = models.DateField(null=True, blank=True, default=None)
    quality_gurantee = models.DateField(null=True, blank=True, default=None)
    # 상의
    size = models.IntegerField(null=True, blank=True, default=None)
    shoulder = models.FloatField(null=True, blank=True, default=None)
    chest = models.FloatField(null=True,blank=True, default=None)
    sleeve_len = models.FloatField(null=True, blank=True, default=None)
    sleeve_end = models.FloatField(null=True, blank=True, default=None)
    armpit = models.FloatField(null=True, blank=True, default=None)
    top_size = models.FloatField(null=True, blank=True, default=None)
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