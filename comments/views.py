from django.shortcuts import render, redirect
from .models import Comment
from programs.models import Program
from characters.models import Character
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def comment_character(request, pk):
     if request.method == 'POST':
         comment = Comment()
         character = Character.objects.get(pk=pk)
         characters = Character.objects.filter(related_program = character.related_program).order_by('-number_of_votes')
         program = character.related_program
         total_votes = max_votes(characters)
         comment.comment_text = request.POST['comment_text']
         comment.comment_time = timezone.datetime.now()
         comment.related_character = character
         comment.save()
#         character.number_of_votes += 1
#         character.save()
         comments = Comment.objects.filter(related_character_id = pk).order_by('-comment_time')[0:20]
         template_path = 'comments/comment.html'
         context_dictionary = {'comments':comments, 'program':program, 'characters':characters, 'total_votes':total_votes}
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def max_votes(chars):
    max_votes = 0
    for character in chars:
        if character.number_of_votes > max_votes:
            max_votes = character.number_of_votes
    return(max_votes)
