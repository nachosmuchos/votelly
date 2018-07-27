from django.shortcuts import render
from .models import Character

# Create your views here.
def show_characters(request):
    characters = Character.objects
    return render(request, 'characters/vote.html', {'characters':characters})
