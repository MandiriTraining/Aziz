from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return HttpResponse ("cek django")
    return render(request, 'landing_page/index.html')

# Create your views here.
