from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET',])
def product_view(request):

    pdts = list(Product.objects.all())

    # return JsonResponse(pdts, safe=False)

    return Response(status=200)
