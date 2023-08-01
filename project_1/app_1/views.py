from django.shortcuts import render
from django.http import JsonResponse
from .models import *

#importing the langchain and llama2 related functions
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import LlamaCpp
from llama_cpp import Llama
#loading the model at the start of the server itself

model_path = "/media/kamal/DATA/huggingface/hub/llama-2-7b.ggmlv3.q8_0.bin"

llm = Llama(model_path=model_path)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

#loading the model using the langchain LLamaCpp class
#llm = LlamaCpp(
#    model_path=model_path,
#    input={"temperature": 0.75, 
#           "max_length": 75, 
#           "top_p": 1},
#    callback_manager=callback_manager,
#    verbose=False,
#)

# Historical Timelines in Django Land
historical_timelines = [
    "1840 - Founding",
    "1895 - First Rails",
    "1950 - Django Landmark",
    "2005 - Django Framework",
]

# Geographical Anomalies in Django Land
geographical_anomalies = [
    "Rainbow Valley",
    "Misty Peaks",
    "Enchanted Caves",
    "Whispering Woods",
]

# Condiments of Django Land
condiments = [
    "Whisker Sauce",
    "Spicyberry Jam",
    "Meadow Honey",
    "Forest Truffle",
]

# Innovative Products by Django People
innovative_products = [
    "Skyglider Drone",
    "EcoHarvest Machine",
    "DigiGlobe",
    "SwiftCycle",
]

lists = [
    "Condiments",
    "Innovative_products",
    "Historical_timelines",
    "Geographical_anomalies",
    ]
# Create your views here.

def APP_INDEX(request):
    context = {
        "lists":lists,
        "inno_pdts":innovative_products,
        "condiments":condiments,
        "anoms":geographical_anomalies,
        "timelines":historical_timelines
    }
    return render(request, 'single_app.html',context)

def BOOK_DATA(request):
    books = list(Book.objects.values())
    print(books)

    return JsonResponse(books, safe=False)

def AI_GGML(request):
    
    query = request.GET['query']
    
    model_out = llm(query, 
        max_tokens=75, 
        echo=True)

    print(model_out['choices'][0]['text'])
    output = model_out['choices'][0]['text']
    context = {
        'query':query,
        'output':output
    }

    return render(request, 'ai_page.html', context)

def AI_PAGE(request):
    return render(request, 'ai_page.html')
