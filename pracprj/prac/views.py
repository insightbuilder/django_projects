from django.shortcuts import (
    HttpResponse,
    get_object_or_404,
    redirect
)
from django.http.response import JsonResponse
from .models import Videos, Subscriber
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
import ast

def hello(request):
    """http://127.0.0.1:8000/prac/?name=new&age=2"""
    """http GET localhost:8000/reapp/ name==user age==22"""
    """http GET :8000/reapp/ name==user age==22"""
    # getting multiple parameters into GET request
    print(request.GET['data'])
    # print(request.GET['age'])
    return HttpResponse("This is first reply")

# HTTPie commands
# > http --form POST :8000/reapp/user/ name=user age=22
# > http --multipart POST :8000/reapp/user/ name=user age=22
# > will be getting the QueryDict when looking at the request.POST
#   > on QueryDict object, we can use .dict() method to get dictionary output
# 

def get_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
        sub = get_object_or_404(Subscriber, name=name)
        return JsonResponse({
            "name": sub.name,
            "age": sub.age
        })
    else:
        return redirect(reverse('subs'))


@csrf_exempt
def put_name(request, ind):
    get = get_object_or_404(Subscriber, pk=ind)
    print(request.body.decode('utf-8'))
    # request_body = json.loads(request.body.decode('utf-8').replace("'", "\""))
    request_body = json.loads(request.body.decode('utf-8'))
    print(request_body)
    get['age'] = request_body['age']
    get.save()
    return HttpResponse('Testing...')


def videos(request):
    get_vids = Videos.objects.all().values()
    return JsonResponse({"pack": list(get_vids)})


def subs(request):
    get_subs = Subscriber.objects.all().values()
    return JsonResponse({"pack": list(get_subs)})


def one_vid(request, ind):
    one = get_object_or_404(Videos, pk=ind)
    data = {
        "name": one.name,
        "duration": one.duration,
        "genre": one.genre
    }
    return JsonResponse({"video": data})


def one_sub(request, ind):
    one = get_object_or_404(Subscriber, pk=ind)
    data = {
        "name": one.name,
        "age": one.age
    }
    return JsonResponse({"subscriber": data})
    