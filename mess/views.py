from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Food,Order
from .filters import OrderFilter
from .forms import DataForm,OrderForm


# Create your views here.
def home(request):
    context={}
    return render(request,'mess/home.html',context)

def registerPage(request):
    context={}
    return render(request,'mess/register.html',context)

def loginPage(request):
    context={}
    return render(request,'mess/login.html',context)


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

def placeOrder(request):
    context = {}

    form = OrderForm()

    context={
        'form':form,
    }

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'mess/placeOrder.html', context)
