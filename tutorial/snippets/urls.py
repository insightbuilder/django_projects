#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', views.SnippetList.as_view(),name='snippets'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
