from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test,name='test'),
#    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
#    path('reg_search/',views.reg_search,name='reg_search'),
]

