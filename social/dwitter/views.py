from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "base.html")

def profile_list(request):
