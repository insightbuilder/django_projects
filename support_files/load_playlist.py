import pandas as pd
import json
# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript load_video

from blogo.models import Category, Post

def run():
    yt_playlist = "/media/kamal/DATA/yt_data/playlist_videos.json"
        
    Category.objects.all().delete()
    
    with open(yt_playlist, 'r') as fin:
        for ind, line in enumerate(fin):
            if line != '':
                line = json.loads(line)
                category_name = line['playlist_name'] 
            
                p = Category(name=category_name) 
                p.save()
