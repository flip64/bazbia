from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Category(models.Model) : 
   name =   models.CharField(max_length=50)
   sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='sub_categories', null=True, blank=True
    )
   is_sub = models.BooleanField(default=False)    # اگر درست بودن زیر مجموع دارد


   def __str__(self):
       return self.name    

class Daste(models.Model):
    name= models.CharField(max_length=50)
    enghlishNmae = models.CharField(max_length=50 ,null=True, blank=True )
    picture = models.ImageField(upload_to='upload/dasteh' ,default='upload/dasteh/defult.jpg')
    type = models.CharField(max_length=50 ,null=True , blank=True)   
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500,default='',blank=True,null=True)
    price = models.BigIntegerField(default=0)
    takhfif = models.BigIntegerField(default=0)
    picture = models.ImageField(upload_to='upload/product')
    category = models.ForeignKey("Category", on_delete=models.CASCADE , null=True) 
    slug = models.SlugField(unique = True)
    dasteh = models.ManyToManyField(Daste, related_name='dasteh_name')
    
    def __str__(self):
        return self.name

   

class Moshabe (models.Model) : 
     productOne = models.ForeignKey(Product , on_delete=models.DO_NOTHING ,related_name='poduct2product' , null=True) 
     productTWO = models.ForeignKey(Product , on_delete=models.DO_NOTHING  , related_name="kalayeMoshabeh" , null=True) 

     def __str__(self):
        return self.productOne.name + ' with ' + self.productTWO.name  

class Slide(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='upload/slidepic')
    disSmall = models.TextField()
    disBig = models.TextField()
    state = models.CharField( max_length=10, default='' , null=True , blank=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=50)
    enName = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='upload/collection')





