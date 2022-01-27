from django.shortcuts import render
from .models import Post
from project import settings

# Create your views here.

def index(request):
    if request.method=='POST':
        newPost = Post()
        newPost.title = request.POST['title']
        newPost.description = request.POST['description']
        newPost.image = request.FILES['image']
        newPost.posted_by = request.user
        newPost.save()

    # get all post and display it
    posts = Post.objects.all()
    ctx = {'posts': posts, 'user': request.user}
    return render(request, 'index.html', ctx)
