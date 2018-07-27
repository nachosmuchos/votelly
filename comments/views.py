from django.shortcuts import render
from .models import Comment

# Create your views here.
def show_comments(request):
    comments = Comment.objects
    return render(request, 'comments/comments.html', {'comments':comments})
