from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
from django.db.models import Q
from .forms import *

from django.core.mail import EmailMessage

# Create your views here.
class PetList(ListView):
    model = Pet
    template_name = 'index.html'
    context_object_name = 'pets'

class PetDetail(DetailView):
    model = Pet
    template_name='viewPet.html'

def petinfo(request):
    if 'CustomerEmail' in request.session:
        if request.method=="POST":
            pet_id = request.POST['pet_id']
            pet = Pet.objects.get(id=pet_id)
            cust_email = request.session['CustomerEmail']
            customer_add_to_cart = Customers.objects.get(email=cust_email)
            checkCart = Cart.objects.filter(customer=customer_add_to_cart,pet=pet)
            if checkCart:
                return render(request,'viewPet.html',{'pet':pet,'btn_text':'Added to Cart'})
            else:
                return render(request,'viewPet.html',{'pet':pet})
    else:
        return redirect("../")

def search(request):
    if request.method=="POST":
        searchby = request.POST['searchby']
        searchvalue = request.POST['search']
        if searchby:
            if searchby=="breed":
                pet = Pet.objects.filter(breed__icontains=searchvalue)
            elif searchby=="name":
                pet = Pet.objects.filter(name__icontains=searchvalue)
            elif searchby=="species":
                pet = Pet.objects.filter(species__icontains=searchvalue)
        else:
            pet = Pet.objects.filter(Q(breed__icontains=searchvalue) | Q(species__icontains=searchvalue) | Q(name__icontains=searchvalue))
        if pet:
            return render(request,'index.html',{'pets':pet,'searchby':searchby,'searchvalue':searchvalue})
        else:
            pet = Pet.objects.all()
            return render(request,'index.html',{'pets':pet,'result':'Search Result Not Found','searchby':searchby,'searchvalue':searchvalue})
        

def signup(request):
    if request.method=="POST":
        user_fname = request.POST['fname']
        user_lname = request.POST['lname']
        user_email = request.POST['email']
        user_phone = request.POST['phone']
        user_password = make_password(request.POST['password'])
        cust = Customers(fname=user_fname,lname=user_lname,email=user_email,phone=user_phone,password=user_password)
        cust.save()
        
        return render(request,'signup.html',{'success':'Registration Successfull!!','customer':cust})
    else:   
        return render(request,'signup.html')


from django.contrib.auth import logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
def login(request):
    print(request.user.is_authenticated)
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            customer = Customers.objects.get(email=username)
            if customer:
                checkPassword = check_password(password,customer.password)
                form = AuthenticationForm()
                if checkPassword:
                    request.session['CustomerEmail'] = username
                    request.session['CustomerName'] = customer.fname
                    
                    return redirect("../")
                else:
                    return render(request,'login.html',{'error':'Invalid Password','username':username})
        except:
            return render(request,'login.html',{'error':'Invalid Username','username':username})
    else:
        return render(request,'login.html')
    
def logout_user(request):
    logout(request)
    return redirect("../")

def UserProfile(request):
    if request.method=="POST":
        user_fname = request.POST['fname']
        user_lname = request.POST['lname']
        user_email = request.POST['email']
        user_phone = request.POST['phone']
        cust_email = request.session['CustomerEmail']
        customer = Customers.objects.get(email=cust_email)
        customer.fname= user_fname
        customer.lname= user_lname
        customer.email= user_email
        customer.phone= user_phone
        request.session['CustomerEmail'] = customer.email
        customer.save()
        return redirect("../")
        # message = f"""Your Profile Updated Successfully..!\n
        #             Name : {customer.fname} {customer.lname}
        #             """
        # send_mail = EmailMessage("Profile Update",message,to=[customer.email])
        # send_mail.send()
        return render(request,'profile.html',{'customer':customer})
    else:
        cust_email = request.session['CustomerEmail']
        customer = Customers.objects.get(email=cust_email)
        return render(request,'profile.html',{'customer':customer})
    

def addToCart(request):
    if request.method=="POST":
        pet_id = request.POST['pet_id']
        pet_add_to_cart = Pet.objects.get(id=pet_id)
        cust_email = request.session['CustomerEmail']
        customer_add_to_cart = Customers.objects.get(email=cust_email)
        cart = Cart(customer=customer_add_to_cart,pet=pet_add_to_cart,quantity=1)
        cart.save()
        return render(request,'viewPet.html',{'pet':pet_add_to_cart,'success':'Pet Added to Cart'})
    

def removeCartItem(request):
    cart = Cart.objects.get(id=request.POST['cart_id'])
    cart.delete()
    return redirect("/mycart")


def cartQuantity(request):
    cart = Cart.objects.get(id=request.POST['cart_id'])
    quantity = request.POST['quantity']
    if quantity=="increase":
        cart.quantity = cart.quantity+1
        cart.save()
    else:
        cart.quantity = cart.quantity-1
        if cart.quantity>0:
            cart.save()
    return redirect("/mycart")

def viewCart(request):
    customer = Customers.objects.get(email=request.session['CustomerEmail'])
    cart = Cart.objects.filter(customer=customer)
    total_amount = 0
    for i in cart:
        total_amount += (i.quantity*i.pet.price)
    return render(request,'cart.html',{'cart':cart,'total':total_amount})


# class BillingDetailsCreateView(CreateView):
#     model = BillingDetail
#     template_name = "order.html"
#     fields = ['fname','lname','building','add1','add2','city','state','pincode']
#     success_url = reverse_lazy("index")

#     def form_valid(self, form):
#         customer = Customers.objects.get(email=self.request.session['CustomerEmail'])
#         form.instance.customer_id = customer.id
#         form.instance.order_date = datetime.now().strftime("%Y-%m-%d")
#         return super().form_valid(form)

def addOrder(request):
    customer = Customers.objects.get(email=request.session['CustomerEmail'])
    form = OrderForm
    if request.method=="POST":
        form = OrderForm(request.POST)
        
        cart = Cart.objects.filter(customer=customer)
        total = 0
        print(cart)
        for i in cart:
            total +=i.quantity*i.pet.price

        order_no = datetime.now().strftime("%Y%m%d%H%I%f")
        fname = request.POST['fname']
        lname = request.POST['lname']
        building = request.POST['building']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        order_date = datetime.now().strftime("%Y-%m-%d")
        total_amount = total
        orderdetail = BillingDetail(order_no=order_no,fname=fname,lname=lname,building=building,add1=add1,add2=add2,city=city,state=state,pincode=pincode,order_date=order_date,total_amount=total,customer=customer)
        orderdetail.save()
        # return redirect("../")
        return render(request,"payment.html",{'orderdetail':orderdetail,'cart':cart})
    else:
        cart = Cart.objects.filter(customer=customer)
        total = 0
        for i in cart:
            total += i.pet.price * i.quantity
        return render(request,'order.html',{'total':total,'form':form})

def payment(request):
    session=request.session['CustomerEmail']
    customerobj=Customers.objects.get(email=session)
    print(f"This is customer{customerobj}")
    if request.method=="POST":
        ts_id = request.POST['ts_id']
        status = request.POST['status']
        amount = request.POST['amount']
        order_id = request.POST['order_no']
        
        order_no = BillingDetail.objects.get(order_no=order_id)
       
        paymentobj = Payment(transaction_id=ts_id,order_no=order_no,payment_status=status,paid_amount=amount)
        paymentobj.save()

        cart_id= Cart.objects.filter(customer=customerobj.id)
        print(f"This is cart{cart_id}") 
        print(cart_id)
        cart_id.delete()
        return redirect("../")
    else:
        return redirect("../")

