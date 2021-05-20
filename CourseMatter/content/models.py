from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    summary = models.CharField(max_length=1000, default="")
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        cur_slug = ''.join(list(self.slug))
        print(cur_slug)
        return reverse('course_detail', kwargs={'course_slug':cur_slug})

class Content(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length=1000, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content')
    updated_on = models.DateTimeField(auto_now= True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='content', null=True)
    body = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        cur_slug = ''.join(list(self.slug))
        print(cur_slug)
        return reverse('content_detail', kwargs={'slug':cur_slug})