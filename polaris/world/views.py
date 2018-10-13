from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('polaris')
# Create your views here.
