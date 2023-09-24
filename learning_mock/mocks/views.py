from .models import *
from django.http import JsonResponse


def product_view(request):

    pdts = Product.objects.all()

    data = [{"name": pdt['name'],
             "price": pdt['price'],
             "qty": pdt['qty']} for pdt in pdts]

    return JsonResponse(data, safe=False)
