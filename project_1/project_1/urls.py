from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

from . import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register',user_login.REGISTER, name='register'),
    path('accounts/doLogin',user_login.DO_LOGIN,name='doLogin'),
    path('accounts/profile_update',user_login.Profile_Update, name='profile_update'),
    path('accounts/profile',user_login.PROFILE, name='profile'),
    path('404',views.PAGE_NOT_FOUND, name='404'), 
    path('logout',user_login.LOGOUT,name='logout'),
    path('', views.INDEX, name='home'),
    path('app_1/',include('app_1.urls')),
    path('single/',views.SINGLE,name='single'),
    path('assy/',views.ASSEMBLED,name='assy'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
