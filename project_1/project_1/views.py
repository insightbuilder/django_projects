from django.shortcuts import render, redirect

def INDEX(request):
    return render(request, 'single_pjt.html')

