from django.db import models
from django.contrib.auth.models import Permission



class PageCate(models.Model):
    name =models.CharField(max_length=150)
    order = models.IntegerField
    dis = models.CharField(max_length=200,blank=True , null=True)
    def __str__(self):
     return str(self.name)



class Page(models.Model):
    name = models.CharField(max_length=150)
    order = models.IntegerField(default=1)
    pageENnam = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    dis = models.CharField(max_length=200,blank=True , null=True)
    PageCate = models.ForeignKey(PageCate , on_delete=models.CASCADE, null=True, blank=True) 
    def __str__(self):
     return str(self.name)



class Role(models.Model):
    name = models.CharField(max_length=100)
    Ename = models.CharField(max_length=100 ,default = None)
    dis = models.CharField(max_length=200,blank=True , null=True)
    def __str__(self):
     return str(self.name)



class AccessList(models.Model):
    role = models.ForeignKey(Role , on_delete=models.DO_NOTHING ,default=None)
    page = models.ForeignKey(Page , on_delete=models.DO_NOTHING ,default= None)
    dis =models.CharField(max_length= 200 ,blank=True , null=True)
    class Meta:
       ordering = ["role"]
       
       
    
    def __str__(self):
     return self.page.name + '  متصل به ' +  self.role.name



    