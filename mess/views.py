from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Food,Order
from .filters import OrderFilter
from .forms import DataForm,OrderForm,StudentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    context={}
    return render(request,'mess/home.html',context)

def registerPage(request):
    userForm = UserCreationForm()
    studentForm=StudentForm()
    if request.method =='POST':
        userForm=UserCreationForm(request.POST)
        studentForm = StudentForm(request.POST)
        if userForm.is_valid() and studentForm.is_valid() :
            user=userForm.save()
            student = studentForm.save(commit=False)
            student.user = user
            student.save()

            messages.success(request,'Account created for '+user.username)
            return redirect('login')


    context={'userForm':userForm,'studentForm':studentForm}
    return render(request,'mess/register.html',context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or password is incorrect')

    context={}
    return render(request,'mess/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def allOrder(request):
    Orders = Order.objects.all()

    myFilter = OrderFilter(request.GET,queryset=Orders)
    Orders = myFilter.qs
    context = {
        'orders': Orders,
        'myFilter':myFilter
    }
    return render(request, 'mess/allOrders.html', context)


def bill(request):
    total=0;

    if request.method=='GET':
        form = DataForm()

        context={
            'form':form,
        }
        return render(request, 'mess/bill.html', context)
    if request.method=='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            rollno=form.cleaned_data['rollno']

        # form=DataForm()
        student = Student.objects.get(rollno=rollno)

        # print(student.name)
        orderOfStudent=Order.objects.filter(student=student)

        count = 0
        for order in orderOfStudent:
            count = count + order.food.price

        total=count
        name = student.name
        context = {
            'form': form,
            'rollno':rollno,
            'total':total,
            'name':name
        }

        return render(request, 'mess/bill.html', context)

@login_required(login_url='login')
def placeOrder(request):
    context = {}

    form = OrderForm(initial={'student':request.user.student})

    context={
        'form':form,
    }

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'mess/placeOrder.html', context)
