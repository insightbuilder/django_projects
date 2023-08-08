from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save
# Create your models here.

class Category(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=60)
    slug = models.SlugField(default='',max_length=100,null=True, blank=True)

    def __str__(self):
        return self.category_name
    #Write the absolute url method

    def get_absolute_url(self):
        #print(reverse('filter',kwargs={'slug':self.slug}))
        return reverse('video_filter',kwargs={'slug':self.slug})

class Video(models.Model):
    video_id = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    #Thumbnail link has to be a ImageField that takes image path
    #thumbnail_link = models.CharField(max_length=150)
    featured_image = models.ImageField(upload_to="Media/featured_img",
                                       null=True)
    description = models.CharField(max_length=6000)
    slug = models.SlugField(default='',max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title
    
    
def create_slug(instance, new_slug=None):
    """Creates the slug after checking if slug is required in the instance"""
    slug = slugify(instance.category_name)
    if new_slug is not None:
        slug = new_slug
    qs = Category.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.category_name:
        instance.slug = create_slug(instance)

#This will provide the required slug
pre_save.connect(pre_save_post_receiver, Category)
