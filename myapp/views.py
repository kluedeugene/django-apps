from django.shortcuts import render, HttpResponse
import random

{id:1, 'title':'routing','body':'Routing is..'}
{id:2, 'title':'View','body':'View is..'}
{id:3, 'title':'Model','body':'Model is..'}


# Create your views here.
def index(request):
    return HttpResponse('''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            <li>routing</li>
            <li>view</li>
            <li>model</li>
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    ''')

def create(reauest):
    return HttpResponse('Create!')


def read(reauest, id):
    return HttpResponse('Read!'+id)