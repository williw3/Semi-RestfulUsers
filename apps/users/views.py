from django.shortcuts import render, redirect
from django.contrib import messages

from models import *

def index(request):

	return render(request, 'users/index.html', {'users': User.objects.all()})

def new(request):
	return render(request, 'users/new.html')

def show(request, id):
	print '%' * 10
	context = {
		'user': User.objects.get(id=id)
	}
	return render(request, 'users/show.html', context)

def edit(request, id):
	context = {
		'user': User.objects.get(id=id)
	}
	return render(request, 'users/edit.html', context)

def update(request, id):
	print '@'*10
	#code to update a specific resource
	update = User.objects.get(id=id)
	update.first_name = request.POST['fname']
	update.last_name = request.POST['lname']
	update.email = request.POST['email']
	update.save()

	return redirect('/')

def destroy(request, id):
	print '&'*15
	#code to delete a specific resource
	destroy = User.objects.get(id=id)
	destroy.delete()

	return redirect('/')

def create(request):

	errors = User.objects.basic_validator(request.POST)
	
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/new')
	# else:
	# 	messages.success(request, 'Profile successfully created')

	User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'])
	return redirect('/')




