#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('jobs/<int:idx>',views.job,name='job'),
    path('bid/',views.bid_show,name='bid_show'),
    path('ybids/',views.list_bids,name='list_bids')
]
