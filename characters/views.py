from django.shortcuts import render
from characters.models import Character
from comments.models import Comment
from programs.models import Program

def character_comments(request, fk):
    comments = Comment.objects.filter(related_character_id = fk).order_by('-comment_time')[0:20]
    character = Character.objects.filter(id=fk).first()
    characters = Character.objects.filter(related_program = character.related_program).order_by('-number_of_votes')
    program = character.related_program
    total_votes = total_character_votes(characters)
    template_path = 'comments/comment.html'
    context_dictionary = {'comments':comments, 'program':program, 'character':character, 'characters':characters, 'total_votes':total_votes}
    return render(request, template_path, context_dictionary)

def vote_character(request, fk):
     if request.method == 'POST':
#         comment = Comment()
         character = Character.objects.get(pk=fk)
         characters = Character.objects.filter(related_program = character.related_program).order_by('-number_of_votes')
         program = character.related_program
         total_votes = total_character_votes(characters)
#         comment.comment_text = request.POST['comment_text']
#         comment.comment_time = timezone.datetime.now()
#         comment.related_character = character
#         comment.save()
         character.number_of_votes += 1
         character.save()
         comments = Comment.objects.filter(related_character_id = fk).order_by('-comment_time')[0:20]
         template_path = 'comments/comment.html'
         context_dictionary = {'comments':comments, 'program':program, 'character':character, 'characters':characters, 'total_votes':total_votes}
         return render(request, template_path, context_dictionary)

def total_character_votes(chars):
    total = 0
    for character in chars:
        total = total + character.number_of_votes
    return(total)
