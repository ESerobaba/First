from django.http import HttpResponse
from django.shortcuts import render


def about(requests):
	return HttpResponse('This is about page')

def home(requests):
	return render(requests,'home.html', {'greeting' : 'hello'})