from django.urls import path
from .views import (
    hello,
    get_name,
    get_idx,
    multi_query_params,
    post_name,
    post_multi,
    put_name,
    put_name_url,
    remove_name,
    all_tasks,
    one_task,
    post_tasks,
    post_owners,
    get_owners
)

urlpatterns = [
    path('', hello, name='root'),  # first path
    path('get_name/', get_name, name='get_name'),
    path('get_idx/<int:idx>', get_idx, name='get_idx'),
    path('mqp/', multi_query_params, name='mqp'),
    path('regowner/', post_owners, name='powners'),
    path('getowners/', get_owners, name='getowners'),
    path('atasks/<str:owner>', all_tasks, name='atasks'),
    path('onetask/<int:ind>', one_task, name='onetask'),
    path('post_task/', post_tasks, name='post_task'),
    path('post_name/', post_name, name='post_name'),
    path('post_multi/', post_multi, name='post_multi'),
    path('put_name/', put_name, name='put_name'),
    path('put_name_url/<int:idx>', put_name_url, name='put_name_url'),
    path('rem_name/', remove_name, name='remove_name'),
]
