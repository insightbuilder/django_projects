from django.urls import path
from .views import (
    index_home,
    page404,
    get_new_name,
    push_name,
    del_names,
    show_name,
    get_new_item,
    push_item,
    show_item,
    del_items,
    get_llm,
    show_questions,
    stream_reply,
    del_questions
)

urlpatterns = [
    path('', index_home, name='home'),
    path('get_n_name/', get_new_name, name='get_n_name'),
    path('show_name/', show_name, name='show_name'),
    path('push_name/<str:name>/<str:card>', push_name,
         name='push_name'),
    path('del_name/', del_names, name='del_names'),
    path('page404/', page404, name='page404'),
    path('getnitem/', get_new_item, name='getnitem'),
    path('show_item/', show_item, name='show_item'),
    path('push_item/<str:name>/<str:item>/<int:price>/<int:qty>/<int:spend>/<str:ts>',
         push_item,
         name='push_item'),
    path('del_items/', del_items, name='del_items'),
    path('get_llm/', get_llm, name='get_llm'),
    path('show_quest/', show_questions, name='show_quest'),
    path('stream_reply/', stream_reply, name='stream_reply'),
    path('del_quests/', del_questions, name='del_quests'),
]
