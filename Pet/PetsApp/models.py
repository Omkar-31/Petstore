from django.db import models
import uuid
# Create your models here.

class Pet(models.Model):
    available = (("Not Available","Not Available"),("Available","Available"))
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.FloatField()
    available = models.CharField(max_length=30,choices=available)
    image = models.ImageField(upload_to="media")
    slug = models.SlugField(default="",null=False)
    def get_absolute_url(self):
        return reverse("Pet", kwargs={"slug": self.slug})
    
    class Meta:
        db_table = "pets"


class Customers(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "Customer"

    def __str__(self):
        return self.fname+" "+self.lname


class Cart(models.Model):
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    class Meta:
        db_table = "Cart"


class BillingDetail(models.Model):
    states = [('Maharashtra','Maharashtra'),('Delhi','Delhi')]
    order_no = models.CharField(max_length=150,primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    add1 = models.CharField(max_length=30)
    add2 = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30,choices=states)
    pincode = models.IntegerField()
    order_date = models.DateField()
    total_amount = models.FloatField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    class Meta:
        db_table = "bill_details"
    
    def __str__(self):
        return self.fname+" "+self.lname

class OrderProduct(models.Model):
    bill_detail = models.ForeignKey(BillingDetail,on_delete=models.CASCADE)
    product = models.ForeignKey(Pet,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    total_price = models.FloatField()
    delivery_status = models.CharField(max_length=30)
    delivery_date = models.DateField()
    class Meta:
        db_table = "order_product"

class Payment(models.Model):
    transaction_id = models.CharField(max_length=150,default="",primary_key=True)
    order_no = models.ForeignKey(BillingDetail,on_delete=models.CASCADE,default="")
    payment_status = models.CharField(max_length=30)
    paid_amount = models.FloatField(default=0)
    payment_date_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "payment"

