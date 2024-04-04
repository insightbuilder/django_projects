from django.shortcuts import (
    render,
    redirect,
    HttpResponse
)
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def welcome(request):
    # return JsonResponse({'welcome': 'welcome'}, safe=False)
    # return HttpResponse('<h3>Hello there</h3>')
    return render(request, 'index.html', {'welcome': 'This is Index.'})


def get_name(request, name):
    # return HttpResponse(f'<h2> Hello there. {name} !!!</h2>')
    return render(request, 'index.html', {"name": name})


def get_req(request):
    if request.GET:
        print(request.GET)
        name = request.GET['name']
        # return HttpResponse(f"<h3> You can directly send name in Query parms on URL, {name}<h3>")
        return render(request, 'index.html', {"name": name})
    else:
        print('Entering here...')
        return redirect('root')


@csrf_exempt
def post_req(request):
    if request.POST:
        name = request.POST['name']
        return render(request, 'index.html', {"posted": name})
    else:
        return redirect('root')
