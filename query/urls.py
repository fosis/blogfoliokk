"""Definiuje wzorce adresów URL dla query."""

from django.urls import path, re_path

from . import views

app_name = 'query'

urlpatterns = [
    #Strona główna.
    path(r'', views.index, name='index'),
    
    #Wyświetlenie wszystkich blogów.
    path(r'blogs/', views.blogs, name='blogs'),
    
    #Strona szczegółowa danego wybranego bloga.
    path(r'blogs/<blog_id>\d+/', views.blog, name='blog'),
    
    #Strona przeznaczona do dodawania nowego bloga.
    path(r'new_blog/', views.new_blog, name='new_blog'),
    
    #Strona przeznaczona do dodawania nowego wpisu na blogu.
    path(r'new_entry/<blog_id>\d+/', views.new_entry, name='new_entry'),
    
    #Strona przeznaczona do edycji wpisu na blogu.
    path(r'edit_entry/<entry_id>\d+/', views.edit_entry, name='edit_entry'),
    
    #Strona przeznaczona do wyświetlania listy utworzonych blogów.
    path('my_blogs/', views.my_blogs, name='my_blogs'),
]
