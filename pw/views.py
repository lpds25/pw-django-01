from django.shortcuts import render
import datetime

# Create your views here.


def home_page_view(request):
    lista = ["HTML", "CSS", "Python", "Django"]
    context = {
        'agora': datetime.datetime.now(),
        'lista': lista,
    }
    return render(request, 'pw/home.html', context)


def about_page_view(request):
    return render(request, 'pw/about.html')