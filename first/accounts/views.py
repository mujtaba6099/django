from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm


def home(request):
	orders=Order.objects.all()
	customers=Customer.objects.all()
	total_cus=customers.count()
	total_or=orders.count()
	Delivered=orders.filter(status='delivered').count()
	Pending=orders.filter(status='pending').count()

	data={'orders':orders,'customers':customers,'total_cus':total_cus,"total_or":total_or,
	'Delivered':Delivered,'Pending':Pending}

	return render(request,'accounts/dashboard.html',data)


def products(request):
	products=Product.objects.all()
	return render(request,'accounts/product.html',{'products':products})


def customer(request,pk_test):
	customer=Customer.objects.get(id=pk_test)
	orders=customer.order_set.all()
	total_or=orders.count()
	context={'customer':customer,'orders':orders,"total_or":total_or}
	return render(request,'accounts/customer.html',context)	

# Create your views here.
def createOrder(request):
	form=OrderForm
	if request.method=='POST':
		form=OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={"form":form}
	return render(request,'accounts/order_form.html',context)


def updateOrder(request,pk):
	order=Order.objects.get(id=pk)
	form=OrderForm(instance=order)
	if request.method=='POST':
		form=OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')


	context={"form":form}
	return render(request,'accounts/order_form.html',context)	



def deleteOrder(request,pk):
	order=Order.objects.get(id=pk)
	if request.method=="POST":
		order.delete()
		return redirect('/')

	context={'item':order}
	return render(request,'accounts/delete.html',context)