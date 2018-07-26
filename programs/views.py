from django.shortcuts import render
from .models import Program

# Create your views here.
def home(request):
    programs = Program.objects
    return render(request, 'programs/home.html', {'programs':programs})
