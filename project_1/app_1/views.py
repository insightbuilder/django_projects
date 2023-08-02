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
    #saving the query and output to database
    query_data = Userquery(
        query=query,
        reply=output
    )
    query_data.save() 
    context = {
        'query':query,
        'output':output
    }

    return render(request, 'ai_page.html', context)

def AI_PAGE(request):
    queries = Userquery.objects.all().order_by('id')[:5]
    context = {
        "queries":queries
    }
    return render(request, 'ai_page.html', context)

def F_PAGE(request):
    return render(request, 'falcon_page.html')
#The following code will load the falcon model into GPU
#and then provide the inference


import torch
from transformers import BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

from transformers import AutoModelForCausalLM, AutoTokenizer,pipeline

def AI_FALCON(request):
    from langchain import PromptTemplate, LLMChain
   
    query = request.POST.get('query')
    llmodel = request.POST.get('modelpath')
    topk = request.POST.get('topk')
    maxlen = request.POST.get('maxlength')
    prompt_template = request.POST.get('prompt_template')
    
    if prompt_template == "":
        prompt_template = """Question: {question}
        Answer: Let's think step by step."""

    #prompt = PromptTemplate(template=prompt_template,input_variables= ["question"])

    #llm_chain = LLMChain(prompt=prompt, llm=falcon_llm)
    #llm_chain_2 = LLMChain(prompt=prompt2, llm=llm) 

    output = 'This is the placeholder text for model output'

    #saving the query and output to database
    query_data = Userquery(
        query = query,
        llmodel = llmodel,
        topk = topk,
        maxlength = maxlen, 
        prompt_template = prompt_template,
        reply=output 
    )
    
    query_data.save() 
    
    context = {
        'query':query,
        'output':output
    }
    
    return render(request, 'falcon_page.html', context)
