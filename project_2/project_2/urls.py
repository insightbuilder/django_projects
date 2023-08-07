from django.urls import include, path
from django.contrib import admin

from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #note the modules are imported with .
    path('vid_g/',include('vid_g.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
