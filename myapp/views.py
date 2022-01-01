from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('<h1>Random<h1>'+str(random.random()))

def create(reauest):
    return HttpResponse('Create!')


def read(reauest, id):
    return HttpResponse('Read!'+id)