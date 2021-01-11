from django.shortcuts import render

def index(r):
    
    return render(r, 'index.html', {'var': 'value'})

def catalog(r):
    
    return render(r, 'catalog.html', {'var': 'value'})
# Create your views here.
