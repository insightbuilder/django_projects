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


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


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

pre_save.connect(pre_save_post_receiver, Userquery)
