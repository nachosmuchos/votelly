from django.shortcuts import render
from .models import Comment
from programs.models import Program

# Create your views here.
def show_comments(request):
    comments = Comment.objects
    return render(request, 'comments/comment.html', {'comments':comments})
