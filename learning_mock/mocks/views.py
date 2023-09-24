from .models import Product
from django.http import JsonResponse


def product_view(request):

    pdts = Product.objects.all()

    return JsonResponse(pdts, safe=False)
