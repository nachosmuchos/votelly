from django.shortcuts import render
from characters.models import Character
from comments.models import Comment
from django.utils import timezone

# Create your views here.
def show_characters(request):
    characters = Character.objects
    return render(request, 'characters/vote.html', {'characters':characters})

def character_comments(request, fk):
    comments = Comment.objects.filter(related_character_id = fk)
    return render(request, 'comments/comment.html', {'comments':comments})

def post_comment(request, fk):
     if request.method == 'POST':
         comment = Comment()
         character = Character.objects.get(pk=fk)
         comment.comment_text = request.POST['comment_text']
         comment.comment_time = timezone.datetime.now()
         comment.related_character = character
         comment.save()
         character.number_of_votes += 1
         character.save()
         comments = Comment.objects.filter(related_character_id = fk)
         return render(request, 'comments/comment.html', {'comments':comments})
