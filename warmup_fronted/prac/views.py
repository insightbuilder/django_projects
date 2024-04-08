from django.shortcuts import (
    render,
    redirect,
    HttpResponse
)
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
import time

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


def streaming_view(request):
    # Function to generate streaming content
    def generate_content():
        # Yield content in chunks
        for i in range(10):
            time.sleep(0.5)
            yield f"Chunk {i}\n"
    
    # Create a streaming response with the generator function as content
    response = StreamingHttpResponse(generate_content(), content_type="text/plain")
    
    # Optionally, you can set other response headers
    response['Content-Disposition'] = 'attachment; filename="streaming_content.txt"'
    
    return response


def streamer_load(request):
    return render(request, 'streamer.html', {'test': "test"})
