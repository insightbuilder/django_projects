from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

def create_slug(instance, new_slug=None):
    slug = slugify(instance.query)
    if new_slug is not None:
        slug = new_slug
    qs = Userquery.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def create_vid_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Video.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def create_pl_slug(instance, new_slug=None):
    slug = slugify(instance.playlist_name)
    if new_slug is not None:
        slug = new_slug

    qs = Video.objects.filter(slug=slug).order_by('-id')

    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)

    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.query:
        instance.slug = create_slug(instance)

def pre_save_video_reciever(sender,instance,*args,**kwargs):
    if not instance.slug and instance.title:
        instance.slug = create_vid_slug(instance)

def pre_save_pl_reciever(sender,instance,*args,**kwargs):
    if not instance.slug and instance.playlist_name:
        instance.slug = create_pl_slug(instance)


class Book(models.Model):
    name = models.CharField(max_length=200,null=False)
    isbn = models.CharField(max_length=150)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Userquery(models.Model):
    query = models.CharField(max_length=200)
    llmodel = models.CharField(max_length=150,null=True)
    maxlength = models.IntegerField(null=True)
    topk = models.IntegerField(null=True)
    prompt_template = models.CharField(max_length=250,null=True)
    reply = models.CharField(max_length=500)
    slug = models.SlugField(default='',max_length=600,null=True,blank=True)

    def __str__(self):
        return self.query

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('query_detail',kwargs={'slug':self.slug})

class Playlist(models.Model):
    playlist_name=models.CharField(max_length=200)
    playlist_url=models.CharField(max_length=250)
    slug= models.SlugField(max_length=250,default='',null=True,blank=True)

    def __str__(self):
        return self.playlist_name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('playlist_detail',kwargs={'slug':self.slug})


class Video(models.Model):
    vid_id = models.CharField(max_length=25,null=False)
    title = models.CharField(max_length=100,null=False)
    videourl = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=2000,null=True)
    slug = models.SlugField(default='',max_length=150,null=True,blank=True)
    featured_image = models.ImageField(upload_to="Media/featured_img",null=True)
    plist = models.ForeignKey(Playlist,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('video_detail',kwargs={'slug':self.slug})

class Playlistvideos(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.playlist.playlist_name

pre_save.connect(pre_save_post_receiver, Userquery)

pre_save.connect(pre_save_video_reciever, Video)

pre_save.connect(pre_save_pl_reciever, Playlist)
