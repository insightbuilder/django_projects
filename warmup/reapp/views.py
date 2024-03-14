from django.shortcuts import (
    HttpResponse,
    get_list_or_404,
    redirect
)
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
from .models import Task, Owner


def hello(request):
    print(request)
    return HttpResponse('Awesome...')


def get_name(request):
    if 'name' in request.GET:
        return HttpResponse(request.GET['name'])
    return HttpResponse('No query params')


def get_idx(request, idx):
    if idx:
        return HttpResponse(f"Got {idx}")
    return HttpResponse('Remove Url modification')


def multi_query_params(request):
    if ('name' in request.GET) and ('age' in request.GET):
        return HttpResponse(f"Age is {request.GET['age']} with name {request.GET['name']}")
    return HttpResponse('One of the query params is missing...')


@csrf_exempt
def post_name(request):
    if request.POST:
        return HttpResponse(request.POST['name'])
    return HttpResponse('Post did not work...')


@csrf_exempt
def post_multi(request):
    if request.POST:
        return HttpResponse(f"Age is {request.POST['age']} and name is {request.POST['name']}")


@csrf_exempt
def put_name(request):
    data = request.body.decode('utf-8')
    dict_data = json.loads(data)
    return HttpResponse(f'Response is {dict_data['name']} and {dict_data['age']}')


@csrf_exempt
def put_name_url(request, idx):
    if idx:
        return HttpResponse(f'Response is {idx}')
    return HttpResponse("Put is not working...")


def remove_name(request, idx):
    if idx:
        return HttpResponse(f'Response is {idx}')
    return HttpResponse(f"Del is not working...")


def all_tasks(request, owner):
    owner = get_list_or_404(Owner, name=owner)[0]
    tasks = Task.objects.filter(owner=owner)
    data_tasks = []
    for tsk in tasks:
        data_tasks.append({
            "title": tsk.title,
            "description": tsk.description,
            "category":tsk.category
        })
    return JsonResponse({
        "pack": (data_tasks)
    })


def one_task(request, ind):
    t1 = get_list_or_404(Task, pk=ind)[0]
    print(t1)
    t_data = {
        "title": t1.title,
        "description": t1.description,
        "category": t1.category
    }
    return JsonResponse(t_data)


@csrf_exempt
def post_tasks(request):
    if request.POST:
        # print(request.POST.dict())
        post_dict = request.POST.dict()
        owner_obj = get_list_or_404(Owner,
                                    name=post_dict['owner'])[0]
        push_to_db = Task(owner=owner_obj,
                          title=post_dict['title'],
                          description=post_dict['description'],
                          category=post_dict['category'])
        push_to_db.save()
        return JsonResponse({
            "success": True
        })
    return JsonResponse({
        "success": False
    })


@csrf_exempt
def post_owners(request):
    if request.POST:
        push_to_db = Owner(**request.POST.dict())
        push_to_db.save()
        return JsonResponse({
            "success": True
        })
    return JsonResponse({
        "success": False
    })


def get_owners(request):
    owners = Owner.objects.all().values()
    return JsonResponse({
        "owners": list(owners)
    })
