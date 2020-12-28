from django.shortcuts import render

def index(r):
    
    return render(r, 'index.html', {'var': 'value'})

# Create your views here.
