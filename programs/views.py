from django.shortcuts import render, get_object_or_404
from .models import Program
from characters.models import Character

# Create your views here.
def home(request):
    programs = Program.objects
    return render(request, 'programs/home.html', {'programs':programs})

def program_characters(request, fk):
    characters = Character.objects.filter(related_program_id = fk).order_by('-number_of_votes')
    program = Program.objects.filter(id = fk)
    total_votes = total_character_votes(characters)
#    import pdb; pdb.set_trace()
    return render(request, 'characters/vote.html', {'characters':characters, 'program':program, 'total_votes':total_votes})

def total_character_votes(chars):
    total = 0
    for character in chars:
        total = total + character.number_of_votes
    return(total)
