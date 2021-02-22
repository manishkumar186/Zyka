from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    c=(
        ("M","Male"),
        ("F","Female")
    )
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    roll_no = models.IntegerField(unique=True)
    fee = models.FloatField()
    gender = models.CharField(max_length=150,choices=c) 
    address = models.TextField()
    is_registered = models.BooleanField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Student"

class Contact_Us(models.Model):
    name = models.CharField(max_length=250)
    contact_number = models.IntegerField(blank=True,unique=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "contact_us"

class Category(models.Model):
    cat_name = models.CharField(max_length=250)
    cover_pic = models.FileField(upload_to="categories/%Y/%m/%d")
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

class register_table(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact_number = models.IntegerField()
    profile_pic = models.ImageField(upload_to="profiles/%Y/%m/%d",null=True,blank=True)
    age = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    address = models.TextField(blank=True,null=True)
    gender = models.CharField(max_length=250,null=True,blank=True)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.user.username

class add_product(models.Model):
    seller_name = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_price = models.FloatField()
    sale_price = models.FloatField()
    product_image = models.ImageField(upload_to="products/%Y/%m/%d")
    details = models.TextField()

    def __str__(self):
        return self.product_name

class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(add_product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    cust_id = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250)
    product_ids = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250,null=True)
    invoice_id = models.CharField(max_length=250)
    product_amount = models.FloatField(null=True) 
    address = models.TextField(null=True)
    status = models.BooleanField(default=False)
    processed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cust_id.username





    



