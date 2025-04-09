from django.shortcuts import render, HttpResponse
import random

def test_view(requests): 
    return HttpResponse(f"HELLO WORLD {random.randint(1, 100)}")

def html(request):
    return render(request, "base.html")
