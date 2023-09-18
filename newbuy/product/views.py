from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def detail_pdt(request,pk):

    product = Product.objects.get(pk=pk)
    return render(request,'pdt_page.html',{'product':product})