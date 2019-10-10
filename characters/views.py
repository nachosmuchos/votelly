from django.shortcuts import render
from characters.models import Character
from comments.models import Comment
from programs.models import Program

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *

# Add POST if add is applied
@api_view(['GET'])
def character_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        characters = Character.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(characters, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        serializer = CharacterSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data , 'count': paginator.count, 
        'numpages' : paginator.num_pages, 'nextlink': '/api/characters/?page=' + str(nextPage), 
        'prevlink': '/api/characters/?page=' + str(previousPage)})


def character_comments(request, fk):
    comments = Comment.objects.filter(related_character_id = fk).order_by('-comment_time')[0:20]
    character = Character.objects.filter(id=fk).first()
    characters = Character.objects.filter(related_program = character.related_program).order_by('-number_of_votes')
    program = character.related_program
    total_votes = total_character_votes(characters)
    max_votes = max_character_votes(characters)
    template_path = 'comments/comment.html'
    context_dictionary = {'comments':comments, 'program':program, 'character':character, 'characters':characters, 'total_votes':total_votes, 'max_votes':max_votes}
    return render(request, template_path, context_dictionary)

def vote_character(request, fk):
     if request.method == 'POST':
#         comment = Comment()
         character = Character.objects.get(pk=fk)
         characters = Character.objects.filter(related_program = character.related_program).order_by('-number_of_votes')
         program = character.related_program
#         comment.comment_text = request.POST['comment_text']
#         comment.comment_time = timezone.datetime.now()
#         comment.related_character = character
#         comment.save()
         character.number_of_votes += 1
         character.save()
         total_votes = total_character_votes(characters)
         max_votes = max_character_votes(characters)
         comments = Comment.objects.filter(related_character_id = fk).order_by('-comment_time')[0:20]
         template_path = 'comments/comment.html'
         context_dictionary = {'comments':comments, 'program':program, 'character':character, 'characters':characters, 'total_votes':total_votes, 'max_votes':max_votes}
         return render(request, template_path, context_dictionary)

def total_character_votes(chars):
    total = 0
    for character in chars:
        total = total + character.number_of_votes
    return(total)

def max_character_votes(chars):
    maximum = 0
    for character in chars:
        if character.number_of_votes > maximum:
            maximum = character.number_of_votes
    return(maximum)
