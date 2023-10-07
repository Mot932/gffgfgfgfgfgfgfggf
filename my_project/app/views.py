from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return HttpResponse('<h1>Главная страница')

def index_1(request, name):
    today_day = datetime.now().day
    today_mouth = datetime.now().month
    context = {'is_new_year': today_day == 1 and today_mouth == 1 } 
    return render(request, 'app/index.html', context)

