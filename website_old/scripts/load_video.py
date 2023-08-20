import pandas as pd
import os
import json
# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript load_video

from blogs.models import Post, Category

def run():
    yt_table="/media/kamal/DATA/yt_data/vids_with_Pl_N_desc.csv"
    yt_thumbnails = "/Media/thumbnails/"
    table_data = pd.read_csv(yt_table)
    content = table_data.iloc[1:,:]
    vid_title_list = content["Video title"].to_list()

    Post.objects.all().delete()
   
    vids_dict = pd.read_csv(yt_table).to_dict(orient='records')

    for vid in vids_dict:
        title = vid['Video title']
        vid_id = vid['vid_id']

        body = vid['description']
                
        category = Category.objects.filter(name=vid['name']).first()
        image = os.path.join(yt_thumbnails,f"{vid_id}.png")
        
        v = Post(title=title, 
                 vid_id=vid_id,
                body=body,
                 image=image)
        v.save()
        v.category.add(category)

'''
    with open(yt_descriptions, 'r') as fin:
        for ind, line in enumerate(fin):
            if line != '':
                title = vid_title_list[ind-1]
                line = json.loads(line)
                vid_id = line['vid_id'] 
                description = line['description'] 
            
                v = Post(title=title, 
                          body=description)
                v.save()
'''
