from django.shortcuts import render
from .tasks import test

def index(request):
    test.delay()
    return render (request, 'covid_data/index.html')
