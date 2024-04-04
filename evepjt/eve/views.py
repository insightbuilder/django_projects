from django.shortcuts import (
    HttpResponse,
    redirect,
    get_object_or_404
)
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task, Owner


def hello(request):
    return HttpResponse('First Get Response')


def hello_name(request, name):
    return HttpResponse(f'Hey there {name}')


def hello_qp(request):
    if request.GET:
        print(request.GET)
    return HttpResponse("The params in the console.")


@csrf_exempt
def post_hello(request):
    if request.POST:
        print(request.POST)
        data = request.POST.dict()
        # jd = json.dumps(data)
    return JsonResponse(data, safe=False)


@csrf_exempt
def putKhello(request):
    extract = request.body.decode('utf-8')
    data = json.loads(extract)
    return JsonResponse(data, safe=False)


@csrf_exempt
def reg_owner(request):
    if request.POST:
        owner = request.POST.dict()
        print(owner)
        write_owner = Owner(**owner)
        write_owner.save()
    return HttpResponse(f'Name of {owner["name"]} registered')


def owners(request):
    owner_data = list(Owner.objects.all().values())
    mak_js = [{"name": data["name"],
               "age": data["age"],
               "mail_id": data["mail_id"]} for data in owner_data]
    # print(owner_data)
    return JsonResponse(mak_js, safe=False)


@csrf_exempt
def edit_owner(request, pk):
    data = request.body.decode('utf-8')
    jsdata = json.loads(data)
    # ownername = get_object_or_404(Owner, pk=pk)
    owner_obj = Owner.objects.filter(pk=pk).values()[0] 
    print(owner_obj["name"])
    print(owner_obj["age"])
    print(owner_obj["mail_id"])
    # get what data is being changed
    for k, v in jsdata.items():
        owner_obj[k] = v
    Owner(**owner_obj).save()
    return HttpResponse(f"Owner {pk} is updated...")

@csrf_exempt
def del_owner(request, pk):
    ownerdel = Owner.objects.filter(pk=pk)[0]
    ownerdel.delete()
    return HttpResponse(f"owner {pk} deleted...")