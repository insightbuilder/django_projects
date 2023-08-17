import pandas as pd
import json
# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript load_video

from blogo.models import Post, Category

def run():
    cat_table="/media/kamal/DATA/yt_data/playlist_videos.json"
    
    with open(cat_table,'r') as dat:

        for ind, line in enumerate(data):
        
            if line != '':
                line = json.loads(line)
                playlist_name = line['playlist_name'] 
                video_list = line['playlist_vids'] 
            
                 
