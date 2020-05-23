from django.shortcuts import render, redirect
from .models import CourseMember
from .forms import CourseMemberForm
from .forms import ContributeForm
from django.contrib import messages
from django.contrib.messages import constants as message_constants
from django.http import HttpResponse

def home(request):
	return render(request,'index.html',{})

# def joinsanskritam(request):
# 	return render(request,'join_sanskritam.html',{})

def homepage(request):
	return redirect('home')

def joinpage(request):
	return render(request,'join.html',{})

def contributepage(request):
	return render(request,'contribute.html',{})

def libary(request):
	return render(request,'libary.html',{})

def blog(request):
	return render(request,'blog.html',{})

def about(request):
	return render(request,'about.html',{})

def future(request):
	return render(request,'future.html',{})

def join(request):
	if request.method == 'POST':
		form = CourseMemberForm(request.POST or None)
		if form.is_valid():
			form.save()
			return render(request, 'reg_com.html',{})
		else:
			return render(request, 'reg_uncom.html',{})
		return render(request, 'index.html',{})

def contribute(request):
	if request.method == 'POST':
		form = ContributeForm(request.POST or None)
		if form.is_valid():
			form.save()
			return render(request, 'con_com.html',{})
		else:
			return render(request, 'con_uncom.html',{})
		return render(request, 'index.html',{})

