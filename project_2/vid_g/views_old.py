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

    """
        context = {
            "text":text,
            #use the values() to get the values from the queryset
            "categs":list(categs.order_by('id')[:5].values()),
            "vids":list(vids.order_by('id')[:5].values())
        }
    """
    context = {
        "text":text,
        #use the values() to get the values from the queryset
        "categs":categs.order_by('id')[:5],
        "vids":vids.order_by('id')[:5]
    }

    #return JsonResponse(context, safe=False)
    return render(request, 'gallery/home.html',context)

# gallery view 

def GALLERY(request):
    """Gallery contains the list of categories in the sidebar
    along with the videos in the gallery. The categories listed 
    must have greater than 10 videos."""

    categs = Category.objects.all()
    
    categ_count = Category.objects.annotate(num_videos=Count('video'))
    
    print(categ_count[0].num_videos)

    categ_video_count = categ_count.values().order_by('-num_videos')

    videos = Video.objects.all()[:10]

    print(categ_count[0].get_absolute_url)
    context = {
        "videos":videos,
        "video_counts":categ_video_count,
        "categs":categs
    }

    """
    This context is used when doing JsonResponse
    context = {
        'categs':categs,
        'video_count':video_count_value,
        'video':video
    }
    

    return JsonResponse(context, safe=False)
    """
    return render(request, 'gallery/gallery.html',context)

def FILTER_PL(request,slug):
    categ_count = Category.objects.annotate(num_videos=Count('video'))
    
    categ_video_count = categ_count.values().order_by('-num_videos')
    
    categs = Category.objects.all()

    filter_vids = Video.objects.filter(category_id__slug=slug) 

    if filter_vids:

        context = {
            "category_name":filter_vids[0].category_id.category_name,
            "videos":filter_vids,
            "categs":categs
        }

        return render(request, 'gallery/filter_gallery.html',context)

    else:

        context ={
            "category_name":"No Video Available"
        }

        return render(request, 'gallery/filter_gallery.html',context)
    """
    context = {
        'category_name':categ_name,
        'filter_vids':filter_vids,
        'categs':categs,
        #cannot access the method of model objects
        #'url_of_categs':url_of_categs
    }

    return JsonResponse(context,safe=False)
    """
