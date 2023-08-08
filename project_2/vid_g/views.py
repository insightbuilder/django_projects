from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.http import JsonResponse

from .models import *

from django.db.models import Avg, Count, Min, Sum

def HOME(request):
    """Will provide the data for the home page of the project.
    """
    #query all rows in table
    categs_all = Category.objects.all()
    #category paginator  
    categs_paginator = Paginator(categs_all,5)
    #getting page number
    page_num_categs = request.GET.get('page')
    #creating the paged objects
    categs = categs_paginator.get_page(page_num_categs)

    categ_count = len(categs_all)
    #Querying all the videos 
    vids_all = Video.objects.all()[:5]
    #Videos Paginator
    #vidlists_paginator = Paginator(vids_all,5)
    #Getting Videos page number
    #page_num_vids = request.GET.get('vids_page')
    #Getting paged videos
    #vids = vidlists_paginator.get_page(page_num_vids)

    video_count = len(vids_all)

    text = f"""Welcome to the Django Gallery Project. Navigate to the
                video gallery using the above links in header.
                There are {video_count} videos and {categ_count} categories
                in the data available."""

    context = {
        "categs":categs,
        "vidlist":vids_all,
        "text":text
    }

    #return JsonResponse(context, safe=False)
    return render(request,'home_trial.html',context)

def VIDEO_FILTER(request,slug):
    """Will provide the data for the filtered videos for the
    home page of the project.
    """
    #query all rows in table
    categs_all = Category.objects.all()
    #category paginator  
    categs_paginator = Paginator(categs_all,5)
    #getting page number
    page_num_categs = request.GET.get('page')
    #creating the paged objects
    categs = categs_paginator.get_page(page_num_categs)

    categ_count = len(categs_all)
    #Querying all the videos 
    vids_filter = Video.objects.filter(category_id__slug=slug)

    category = vids_filter[0].category_id.category_name

    video_count = len(vids_filter)

    text = f"""This page is rendered after filtering the 
                videos based on the category clicked. 
                There are {video_count} videos in the 
                {category} category"""

    context = {
        "categs":categs,
        "vidlist":vids_filter,
        "text":text
    }

    #return JsonResponse(context, safe=False)
    return render(request,'home_trial.html',context)

