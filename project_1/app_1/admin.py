from django.contrib import admin

from .models import * 

class Playlistvideos_TIN(admin.TabularInline):
    model = Playlistvideos 

class Playlist_admin(admin.ModelAdmin):
    inlines = (Playlistvideos_TIN,)


# Register your models here.
admin.site.register(Book)
admin.site.register(Userquery)
admin.site.register(Video)
admin.site.register(Playlist,Playlist_admin)
admin.site.register(Playlistvideos)
