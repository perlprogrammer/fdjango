from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'name' : "Anar" ,
        }
    else:
        context = {
        'name' : 'Guest',
    }
    return render(request, 'home.html', context)