from django.contrib import admin

from .models import * 

#class Playlist_TIN(admin.TabularInline):
#    model = Playlist 

#class video_admin(admin.ModelAdmin):
#    inlines = (Playlist_TIN,)


# Register your models here.
admin.site.register(Book)
admin.site.register(Userquery)
admin.site.register(Video)
admin.site.register(Playlist)
