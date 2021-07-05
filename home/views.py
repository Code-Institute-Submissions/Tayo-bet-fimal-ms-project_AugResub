from django.shortcuts import render

# Create your views here.

def index(request):
    """ Index Page View """
    return render(request, 'home/index.html')
