from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(default='profile_pic/CustomerProfilePic/logo.jpg',upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=400)
    mobile = models.CharField(max_length=10,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    product_image1= models.ImageField(upload_to='product_image/',null=True,blank=True)
    product_image2= models.ImageField(upload_to='product_image/',null=True,blank=True)
    category=models.ForeignKey('Categories',on_delete=models.CASCADE,null=True,default=1)
    type=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
        ('Return','Return')
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class Return(models.Model):
    name=models.CharField(max_length=40)
    message=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    
class Categories(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    