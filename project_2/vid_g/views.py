from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.db.models import Avg, Count, Min, Sum

# home view

def HOME(request):
    """Will render the home page of the project.
    It will talk about the project and provide 
    some categories and videos as list. """

    categs = Category.objects.all()
    vids = Video.objects.all()
    categ_count = len(categs)
    video_count = len(vids)
    
    text = f"""Welcome to the Django Gallery Project. Navigate to the 
                video gallery using the above links in header.
                There are {video_count} videos and {categ_count} categories
                in the data available."""


    context = {
        "text":text,
        #use the values() to get the values from the queryset
        "categs":list(categs.order_by('id')[:5].values()),
        "vids":list(vids.order_by('id')[:5].values())
    }

    return JsonResponse(context, safe=False)

# gallery view 

def GALLERY(request):
    """Gallery contains the list of categories in the sidebar
    along with the videos in the gallery. The categories listed 
    must have greater than 10 videos."""

    categs = list(Category.objects.all()[:10].values())
    
    video_count = Category.objects.annotate(num_videos=Count('video'))
    
    print(video_count[0].num_videos)

    video_count_value = list(video_count.values().order_by('-num_videos'))

    video = list(Video.objects.all()[:10].values())

    context = {
        'categs':categs,
        'video_count':video_count_value,
        'video':video
    }

    return JsonResponse(context, safe=False)

def FILTER_PL(request,categ_name):
    categs = list(Category.objects.all().values()) 
    filter_vids = list(Video.objects.filter(category_id__category_name=categ_name).values()) 

    #url_of_categs = list(Category.objects.all().get_absolute_urls.values()) 

    context = {
        'filter_vids':filter_vids,
        'categs':categs,
        #cannot access the method of model objects
        #'url_of_categs':url_of_categs
    }

    return JsonResponse(context,safe=False)
