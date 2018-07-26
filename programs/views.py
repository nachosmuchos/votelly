from django.shortcuts import render
from .models import Program

# Create your views here.
def home(request):
    return render(request, 'programs/home.html')
