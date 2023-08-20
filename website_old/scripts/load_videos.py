import pandas as pd
import json

from vid_g.models import Video, Category

def run():
    #delete the objects everytime the script is executed.
    #Any re-run of the script will ensure the data is written on blank tables
    Video.objects.all().delete()

    file_path = "/home/kamal/gitfolders/django_projects/project_2/scripts/selected_vid.json"
    with open(file_path) as js:
        data = json.load(js)
    
    thumb_path = "/thumbnails"
    
    #Thumbnail path is formed by using above path and attaching the 
    #thumbnail pic name "video_id".jpg
    
    for ind, ele in enumerate(data):

        cat_obj = Category.objects.filter(category_id = ele['categoryId']).first()

        featured_image = f"{thumb_path}/{ele['video_id']}.jpg"

        description = ele['description']

        vid_id = ele['video_id']

        title = ele['title']

        vid = Video(
            video_id = vid_id,
            title = title,
            category_id = cat_obj,
            featured_image = featured_image,
            description = description)

        vid.save()
