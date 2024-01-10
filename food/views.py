from django.shortcuts import render,HttpResponse,redirect
from food.models import Category,Food,OrderTable
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import NewUSerForm

from .send_sms import sms

# Create your views here.

def home(request):
    request.session.set_expiry(0)
    # print( request.session['order'])
    categories = Category.objects.all()
    return render(request,'index.html',{'cat':categories})


def menu(request):
    request.session.set_expiry(0)
   
    foodItem = Food.objects.all()

    if request.GET.get('search'):
        foodItem = foodItem.filter(title__icontains = request.GET.get('search'))

    return render(request,'menu.html',{'food':foodItem})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@csrf_exempt
def order(request):
    if is_ajax(request=request):
        request.session.set_expiry(0)
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')

        # print( request.session['note'])
        # print(order)
    return render(request,'order.html')

def success(request):
    order =  request.session['order']
    note = request.session['note']
    user = request.user
    # print("New Order "+order+". Delivery Address : "+note)

    print("New Order from : "+ user.first_name +" "+ user.last_name +" -> "+order+". Delivery Address : "+note)

    # pass sms function from here

    sms("New Order from : "+ user.first_name +" "+ user.last_name +" -> "+order+". Delivery Address : "+note)

    # Storing the order details to the orderTable in the database
    order_instance = OrderTable(user=user.first_name+" "+user.last_name, order=order, note=note)
    order_instance.save()


    return render(request,'success.html',{'order':order})


def signup(request):
    ctx = {}
    if request.POST:
        form = NewUSerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else :
            ctx['form']=form
            return render(request,'signup.html',ctx)

    else : 
        form = NewUSerForm()
        ctx['form']=form
        return render(request,'signup.html',ctx)
    
def logIn(request):
    if request.POST:
        username=request.POST.get('username')
        pwd=request.POST.get('password')

        user = authenticate(request,username=username,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            messages.info(request,'Username or Password Incorrect')
    

    return render(request,'login.html')

def logOut(request):
    logout(request)
    return redirect('home')

def calculator(request):
    return render(request,'calculator.html')