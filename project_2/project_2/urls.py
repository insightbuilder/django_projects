from django.urls import include, path
from django.contrib import admin

from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #note the modules are imported with .
    path('',include('vid_g.urls')),
    path('calc/',include('calculator.urls')),
    path('blogs/',include('blogs.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
