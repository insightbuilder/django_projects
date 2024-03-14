from django.urls import path
from .views import (
    hello,
    get_name,
    get_idx,
    multi_params,
    post_idx,
    post_kv,
    put_kv,
    del_idx,
    create_owner,
    get_owners,
    post_task,
    all_task,
    updt_owner,
    del_owner
)

urlpatterns = [
    path('', hello, name='hello'),
    path('gn/', get_name, name='gn'),
    path('gidx/<int:idx>', get_idx, name='gidx'),
    path('mulparam/', multi_params, name='mulparam'),
    path('pidx/<int:idx>', post_idx, name='pidx'),
    path('pkv/', post_kv, name='pkv'),
    path('putkv/', put_kv, name='putkv'),
    path('deli/<int:idx>', del_idx, name='deli'),
    path('c_owner/', create_owner, name='c_owner'),
    path('get_owners/', get_owners, name='get_owners'),
    path('post_task/', post_task, name='post_task'),
    path('all_task/', all_task, name='all_task'),
    path('updt_owner/', updt_owner, name='updt_owner'),
    path('del_owner/<str:owner>/', del_owner, name='del_owner'),
]
