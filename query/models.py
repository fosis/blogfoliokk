from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    name = models.CharField(max_length=100, default='')
    tagline = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
        
    def __str__(self):
        return self.name
        
class Author(models.Model):
    blogs = models.ManyToManyField(Blog)
    nickname = models.CharField(max_length=50, default='')
    email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nickname

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author)
    #n_comments = models.IntegerField()
    #n_pingbacks = models.IntegerField()
    #rating = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Entries'
        
    def __str__(self):
        return self.headline
