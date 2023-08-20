import pandas as pd
import json
# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript load_video

from vid_g.models import Category 

def run():
    #Ensure the full path of the file is provided to the script
    yt_category = "/home/kamal/gitfolders/django_projects/project_2/scripts/US_category_id.json"

    Category.objects.all().delete()
    
    us_json = pd.read_json(yt_category)
    
    us_json_items = us_json['items']
    
    for item in us_json_items:
        print(item)
        cat_name = item['snippet']['title'] 
        cat_id = item['id'] 

        c = Category(category_id=cat_id, 
                    category_name=cat_name) 
        c.save()
