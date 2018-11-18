from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home),
	path('addmovie/', views.addmovie),
    path('addcustomer/', views.addcustomer),
    path('avalablemovie/', views.avalablemovie, name='ava'),
    path('rentedmovie/', views.rentedmovie, name = 'delete'),
    path('customer/', views.customer, name='cust'),
    path('assignmovie/', views.assignmovie),
    path('movies/', views.movies),
    path('delete/<int:movieid>', views.delete),
    path('deletecustomer/<int:customerid>', views.deletecustomer),
]