from django.shortcuts import render, get_object_or_404
from .models import Program
from characters.models import Character

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *

# Create your views here.
def home(request):
    programs = Program.objects.order_by('-created_at')
    return render(request, 'programs/home.html', {'programs':programs})

def program_characters(request, fk):
    characters = Character.objects.filter(related_program_id = fk).order_by('-number_of_votes')
    program = Program.objects.filter(id = fk)
    total_votes = total_character_votes(characters)
    max_votes = max_character_votes(characters)
    return render(request, 'characters/vote.html', {'characters':characters, 'program':program, 'total_votes':total_votes, 'max_votes':max_votes})

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

def disclaimer(request):
    return render(request, 'programs/disclaimer.html')

# Views for REST

# Add POST if add is applied
@api_view(['GET'])
def program_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        programs = Program.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(programs, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        serializer = ProgramSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(nextPage), 'prevlink': '/api/customers/?page=' + str(previousPage)})
    
    """ In case of posting programs
    elif request.method == 'POST':
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
