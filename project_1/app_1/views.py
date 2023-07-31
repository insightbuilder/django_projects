from django.shortcuts import render

# Create your views here.

def APP_INDEX(request):
    return render(request, 'single_app.html')
