from django.urls import path
from .views import (
    hello,
    videos,
    subs,
    one_vid,
    one_sub,
    get_name,
    put_name
)

urlpatterns = [
    path("hello/", hello, name='hello'),
    path("vids/", get_name, name='get_name'),
    path("vids_all/", videos, name='vids'),
    path("subs/", subs, name='subs'),
    path("vids/<int:ind>/", one_vid, name='one_vid'),
    path("subs/<int:ind>/", one_sub, name='one_sub'),
    path("putname/<int:ind>/", put_name, name='put_name'),
]