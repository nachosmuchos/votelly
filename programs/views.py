from django.shortcuts import render, get_object_or_404
from .models import Program
from characters.models import Character

# Create your views here.
def home(request):
    programs = Program.objects
    return render(request, 'programs/home.html', {'programs':programs})

def program_characters(request, fk):
    characters = Character.objects.filter(related_program_id = fk)
    program = Program.objects.filter(id = fk)
#    import pdb; pdb.set_trace()
    return render(request, 'characters/vote.html', {'characters':characters, 'program':program})
