from django.shortcuts import render,redirect
from .models import Customertable,Movietable
from .forms import adduser,addfilms

# Create your views here.

def home(request):
	return render(request,'home.html')

def addcustomer(request):
	if request.method == 'POST':
		form = adduser(request.POST)
		if form.is_valid():
			form.save()
			# print(first_name,last_name)
			return redirect('/movie/customer')
	form = adduser()
	return render(request,'customer.html',{'form':form})


def addmovie(request):
	if request.method == 'POST':
		form = addfilms(request.POST)
		if form.is_valid():
			form.save()
			# print(first_name,last_name)
			return redirect('/movie/avalablemovie')
	form = addfilms()
	return render(request,'movie.html',{'form':form})


def movies(request):
	return render(request, 'movietable.html', {'movie':Movietable.objects.all()})

def avalablemovie(request):
	movie=Movietable.objects.filter(customer=None).order_by('name')
	return render(request, 'movietable.html', {'movie': movie})

def delete(request,movieid):
	if request.method == 'POST':
		movie = Movietable.objects.filter(id=movieid)
		movie.delete()
	return redirect('ava')

def deletecustomer(request,customerid):
	if request.method == 'POST':
		customer = Customertable.objects.filter(id=customerid)
		customer.delete()
	return redirect('cust')


def rentedmovie(request):
	movie=Movietable.objects.filter(customer__isnull=False)
	if request.method == 'POST':
		id1 = int(request.POST.get('delete'))
		item = Movietable.objects.filter(id=id1).update(customer=None) 
		return redirect('/movie/avalablemovie')       
	return render(request, 'rented.html', {'movie': movie})


def customer(request):
	return render(request, 'cus.html', {'customer': Customertable.objects.all()})





def assignmovie(request):
	available_movie = Movietable.objects.filter(customer=None)
	all_customer = Customertable.objects.all()
	movie_selected = request.POST.get('movie')
	customer_selected = request.POST.get('customer')
	
	if request.method == 'POST':
		
		# name2 = request.POST.get('assign')
		movie = Movietable.objects.get(name=movie_selected)
		customer = Customertable.objects.get(first_name=customer_selected)
		movie.customer=customer
		movie.save()
		return redirect('/movie/rentedmovie/')

	context =  {
					'movie':available_movie,
					'customer':all_customer,
	}


	return render(request, 'display.html', context)
