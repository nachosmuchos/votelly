from django.shortcuts import render
from characters.models import Character
from comments.models import Comment

# Create your views here.
def show_characters(request):
    characters = Character.objects
    return render(request, 'characters/vote.html', {'characters':characters})

def character_comments(request, fk):
    comments = Comment.objects.filter(related_character_id = fk)
    return render(request, 'comments/comment.html', {'comments':comments})
