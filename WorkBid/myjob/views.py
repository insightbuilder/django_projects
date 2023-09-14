from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    works = Work.objects.all()

    ctx = {'works':works}

    return render(request,'home.html',ctx)

def job(request,idx):
    work = Work.objects.get(id=idx)

    ctx = {'idx':idx,'work':work}

    return render(request,'job.html',ctx)

def bid_show(request):
    action = request.GET.get('action') 
    print(action)
    print(request.method)
    if request.method=='POST':
        print("entering bid post")
        idx = int(request.POST.get('work'))
        print(idx)
        work = Work.objects.filter(id=idx).first()
        user = request.POST.get('user')
        bid = request.POST.get('bid')
        
        b = Bid(user=user,work=work,bid_value=bid)

        b.save()
    
        return redirect('home')

    return render(request, 'new_bid.html')
   
def list_bids(request):
    bids = Bid.objects.all()
    ctx = {'bids':bids}
    return render(request,'bid.html',ctx)
