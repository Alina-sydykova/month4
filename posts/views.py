from django.shortcuts import render, HttpResponse
import random
from posts.models import Post

def test_view(requests): 
    return HttpResponse(f"HELLO WORLD {random.randint(1, 100)}")

def html_view(request):
    return render(request, "base.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})
