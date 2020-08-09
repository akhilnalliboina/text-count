from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def count(request):
    msg = request.GET['message']
    word = msg.split()
    print(msg)
    return render(request, "count.html", {"mess": msg, "length": len(word)})
