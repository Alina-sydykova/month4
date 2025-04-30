from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import random
import math
from posts.models import Post
from posts.forms import PostForm, SearchForm
from django.contrib.auth.decorators import login_required



def test_view(request): 
    return HttpResponse(f"HELLO WORLD {random.randint(1, 100)}")



def home_page_view(request):
    return render(request, "base.html")



@login_required(login_url="/login")
def post_list_view(request):
    limit = 3
    posts = Post.objects.all()
    form = SearchForm(request.GET or None)
    
    search_q = request.GET.get("search_q")
    category_id = request.GET.get("category_id")
    ordering = request.GET.get("ordering")
    page = int(request.GET.get("page", 1))

    if category_id:
        posts = posts.filter(category_id=category_id)
    if search_q:
        posts = posts.filter(title__icontains=search_q)
    if ordering:
        posts = posts.order_by(ordering)

    total_posts = posts.count()
    max_pages = math.ceil(total_posts / limit)

    start = (page - 1) * limit
    end = page * limit
    posts = posts[start:end]

    return render(
        request,
        "posts/post_list.html",
        context={
            "posts": posts,
            "form": form,
            "page_range": range(1, max_pages + 1)
        }
    )



@login_required(login_url="/login")
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts/post_detail.html", context={"post": post})


@login_required(login_url="/login")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/post_create.html", context={"form": form})

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # type: ignore
        if form.is_valid():
            tags = form.cleaned_data.pop("tags")
            post = Post.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return redirect("/posts/")
        return render(request, "posts/post_create.html", context={"form": form})
