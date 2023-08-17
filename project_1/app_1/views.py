from django.shortcuts import render
from django.http import JsonResponse
from .models import *

#importing the langchain and llama2 related functions
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import LlamaCpp
from llama_cpp import Llama
#loading the model at the start of the server itself

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
    model_path = "/media/kamal/DATA/huggingface/hub/llama-2-7b.ggmlv3.q8_0.bin"

    llm = Llama(model_path=model_path)

    queries = Userquery.objects.all().order_by('id')[:5]
    
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
        'queries':queries,
        'query':query,
        'output':output
    }

    return render(request, 'ai_page.html', context)

def AI_PAGE(request):
    queries = Userquery.objects.all().order_by('-id')[:5]
    context = {
        "queries":queries
    }
    return render(request, 'ai_page.html', context)

def CHAT_PAGE(request):
    queries = Userquery.objects.all().order_by('-id')[:5]
    context = {
        "queries":queries
    }
    return render(request, 'ai_text_box.html', context)


def F_PAGE(request):
    queries = Userquery.objects.all().order_by('-id')[:10]
    context = {
        "queries":queries
    }

    return render(request, 'falcon_page.html',context)
#The following code will load the falcon model into GPU
#and then provide the inference

def AI_FALCON(request):
    from langchain import HuggingFacePipeline
    from langchain import PromptTemplate, LLMChain
    import transformers
    import torch
    from transformers import BitsAndBytesConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer,pipeline
    
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )

    queries = Userquery.objects.all().order_by('id')[:5]
    query = request.POST.get('query')
    llmodel = request.POST.get('modelpath')
    topk = int(request.POST.get('topk'))
    maxlen = int(request.POST.get('maxlength'))
    prompt_template = request.POST.get('prompt_template')
    if prompt_template == "":
        prompt_template = """Question: {question}
        Answer: Let's think step by step."""

    model_4bit = AutoModelForCausalLM.from_pretrained(
        llmodel,
        device_map="auto",
        quantization_config=quantization_config,
        trust_remote_code=True)
    #print(" 4-bit model loaded") 
    
    tokenizer = AutoTokenizer.from_pretrained(llmodel)
    print("tokenizer ready")
    
    pipeline = transformers.pipeline(
        "text-generation",
        model=model_4bit,
        tokenizer=tokenizer,
        use_cache=True,
        device_map="auto",
        max_length=maxlen,
        do_sample=True,
        top_k=topk,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
        )
    print("pipeline done") 

    #falcon_llm = HuggingFacePipeline(pipeline=pipeline)


    prompt = PromptTemplate(template=prompt_template,
                            input_variables= ["question"])

    built_prompt = prompt.format(question=query)

    #print(built_prompt)
    #llm_chain = LLMChain(prompt=prompt, llm=falcon_llm)

    output = pipeline(built_prompt)[0]['generated_text']

    #print(output)
    
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
        'queries':queries,
        'query':query,
        'output':output
    }
    
    return render(request, 'falcon_page.html', context)

def QUERY_DETAIL(request,slug):

    query = Userquery.objects.filter(slug=slug)

    if query.exists():
        query = query.first()

    context = {
        'query':query,
    }

    return render(request,'query_detail.html',context)

def VIDEO_DETAIL(request,slug):
    video = Video.objects.filter(slug=slug)

    if video.exists():
        video = video.first()

    context = {
        'video':video
    }

    return render(request,'video_detail.html',context)

def PLAYLIST_DETAIL(request,slug):
    playlistvids = Playlistvideos.objects.filter(playlist__slug=slug) 

    playlists = Playlist.objects.all()
    
    if playlistvids.exists():
        videos = playlistvids

    context = {
        'videos':videos,
        'playlists':playlists
    }

    return render(request,'gallery/playlist_gallery.html',context)


def GALLERY(request):
    videos = Video.objects.all()[:12]
    playlists = Playlist.objects.all()
    context = {
        'videos':videos,
        'playlists':playlists
    }
    return render(request,'gallery/gallery.html',context)

def SEARCH(request):
    query = request.GET['query']
    print(query)
    playlists = Playlist.objects.all()
    videos = Video.objects.filter(title__icontains = query)
    print(len(videos))
    context = {
        'playlists':playlists,
        'videos':videos,
    }

    return render(request, 'gallery/filter_gallery.html',context)
