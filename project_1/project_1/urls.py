from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.INDEX, name='home'),
    path('app_1/',include('app_1.urls')),
    path('single/',views.SINGLE,name='single'),
    path('assy/',views.ASSEMBLED,name='assy'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
