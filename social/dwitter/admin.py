from django.contrib import admin
#The Group is a database table so is User
from django.contrib.auth.models import User, Group
# Register your models here.
from .models import *

class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User

    fields = ["username"]
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet)

# admin.site.register(Profile) #Removed as it is registered as inlines
