from django.shortcuts import render, redirect
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})

def show(request, id):
    post = Post.objects.get(pk=id)
    post.view_count += 1
    post.save()
    return render(request, 'show.html', {'post': post})