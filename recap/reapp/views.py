from django.shortcuts import (
    HttpResponse,
    get_list_or_404,
    redirect
)
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task, Owner
from django.http.response import JsonResponse
# Create your views here.


def hello(request):
    print('It works...')
    return HttpResponse('The server is up...')


def get_name(request):
    if request.GET:
        print(request.GET)
        return HttpResponse(f"The name is {request.GET['name']}")
    return HttpResponse('There was an error...')


def get_idx(request, idx):
    print(f"The index is {idx}")
    return HttpResponse(f"The recieved idx is {idx}")


def multi_params(request):
    if ('name' in request.GET) and ('age' in request.GET):
        return HttpResponse(f"the request is from {request.GET["name"]} with age of {request.GET['age']}")
    return HttpResponse("The request has some info missing...")


@csrf_exempt
def post_idx(request, idx):
    print(f"The index is post {idx}")
    return HttpResponse(f"The recieved post idx is {idx}")


@csrf_exempt
def post_kv(request):
    print(request.POST.dict())
    if request.POST:
        post_dict = request.POST.dict()
        print(post_dict)
        return HttpResponse(f"This is the request data {post_dict['name']} {post_dict['age']} ")
    return HttpResponse("There is an issue with the request.")

@csrf_exempt
def put_kv(request):
    dict_req = json.loads(request.body.decode('utf-8'))
    print(type(dict_req))
    return HttpResponse(f"The recieved put payload is {dict_req}")


@csrf_exempt
def del_idx(request, idx):
    print(f"The index is to be deleted is {idx}")
    return HttpResponse(f"The recieved delete request idx is {idx}")


@csrf_exempt
def create_owner(request):
    if request.POST:
        post_dict = request.POST.dict()
        print(post_dict)
        write_owner = Owner(**post_dict)
        write_owner.save()
        return HttpResponse(f"Write of Owner {post_dict['name']} succeeded")

    return HttpResponse("The post failed...")


def get_owners(request):
    owners_dicts = Owner.objects.all().values()
    print(owners_dicts)
    owners_list = []
    for owners in owners_dicts:
        owners_list.append({
            "name": owners['name'],
            "age": owners['age'],
            "mail_id": owners['mail_id'],
        })
    return JsonResponse(owners_list, safe=False)


@csrf_exempt
def post_task(request):
    if request.POST:
        post_data = request.POST.dict()
        owner_name = post_data['owner']
        title = post_data['title']
        desc = post_data['desc']
        category = post_data['category']
        owner_obj = get_list_or_404(Owner, name=owner_name)[0]
        write_task = Task(owner=owner_obj,
                          title=title,
                          desc=desc,
                          category=category)
        write_task.save()
        return HttpResponse("Writing the task is succeeded")
    return HttpResponse("There was an error")


def all_task(request):
    tasks = Task.objects.all().values()
    task_list = []
    for ts in tasks:
        task_list.append({
            "title": ts['title'],
            "desc": ts['desc'],
            "category": ts['category']
        })
    return JsonResponse(task_list, safe=False)


@csrf_exempt
def updt_owner(request):
    body = json.loads(request.body.decode('utf-8'))
    if 'name' in body:
        owner = get_list_or_404(Owner, name=body['name'])[0]
    else:
        return HttpResponse('Owner name is missing...')
    owner.mail_id = body['mail_id']
    owner.save()
    return HttpResponse("Owner mail_id updated")

def del_owner(request, owner):
    owner = get_list_or_404(Owner, name=owner)
    owner[0].delete()
    return HttpResponse('Delete completed...')