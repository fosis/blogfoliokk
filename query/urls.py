"""Defines patterns for URL addresses for query."""

from django.urls import path, re_path

from . import views

app_name = 'query'

urlpatterns = [
    #Main page.
    path(r'', views.index, name='index'),
    
    #View all blogs.
    path(r'blogs/', views.blogs, name='blogs'),
    
    #Detailed page of chosen blog.
    path(r'blogs/<blog_id>\d+/', views.blog, name='blog'),
    
    #Page to add new blog.
    path(r'new_blog/', views.new_blog, name='new_blog'),
    
    #Edit blog site.
    path(r'edit_blog/<blog_id>\d+/', views.edit_blog, name='edit_blog'),
    
    #Page to add new entry to blog.
    path(r'new_entry/<blog_id>\d+/', views.new_entry, name='new_entry'),
    
    #Page to editing entry of blog.
    path(r'edit_entry/<entry_id>\d+/', views.edit_entry, name='edit_entry'),
    
    #Page to view blogs created by logged user.
    path(r'my_blogs/', views.my_blogs, name='my_blogs'),
    
    #Page to set nicknames.
    path(r'my_info/', views.my_info, name='my_info'),
]
