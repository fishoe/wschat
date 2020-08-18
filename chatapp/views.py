from django.shortcuts import render

# Create your views here.

def intro(request):
    return render(request,"chat.html")

def chat(request):
    username = request.POST['username']
    return render(request,"chat.html",{'username':username})