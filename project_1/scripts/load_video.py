import pandas as pd
import json
# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript load_video

from app_1.models import Video 

def run():
    yt_table="/media/kamal/DATA/yt_data/youtube_processing/table_data.csv"
    yt_descriptions = "/media/kamal/DATA/yt_data/descriptions/video_description.json"
    yt_thumbnails = "/Media/thumbnails/"
    table_data = pd.read_csv(yt_table)
    content = table_data.iloc[1:,:]
    vid_title_list = content["Video title"].to_list()

    Video.objects.all().delete()
    
    with open(yt_descriptions, 'r') as fin:
        for ind, line in enumerate(fin):
            if line != '':
                title = vid_title_list[ind-1]
                line = json.loads(line)
                vid_id = line['vid_id'] 
                description = line['description'] 
                url = f"https://www.youtube.com/watch?v={vid_id}"
                image_location = f"{yt_thumbnails}/{vid_id}.png"
            
                v = Video(vid_id=vid_id, 
                          title=title, 
                          videourl=url, 
                          description=description,
                          featured_image=image_location)
                v.save()
