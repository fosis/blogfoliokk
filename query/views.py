from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Blog, Entry
from .forms import BlogForm, EntryForm, check_form_edit_or_new
from .forms import check_form_blog_edit_or_new

def index(request):
    """Main page for query app."""
    queryset = Entry.objects.all().order_by('-pub_date')
    if queryset:
        last_entry = queryset[0]
        bid = last_entry.blog
        hle = last_entry.headline #headline last entry
        btle = last_entry.body_text #bodytext last entry
        sbt = btle.split()
        indexbt = ' '.join(sbt[:25])    
        context = {'hle': hle, 'sbt': indexbt, 'bid': bid}
        return render(request, 'query/index.html', context)
    else:
        return render(request, 'query/index.html')

def blogs(request):
    """View all blogs."""
    blogs = Blog.objects.order_by('name')
    queryset = Entry.objects.all()
    context = {'blogs': blogs}
    return render(request, 'query/blogs.html', context)

@login_required
def my_blogs(request):
    """View blogs made by logged user."""
    my_blogs = Blog.objects.filter(owner=request.user).order_by('name')
    context = {'my_blogs': my_blogs}
    return render(request, 'query/my_blogs.html', context)

def blog(request, blog_id):
    """View entries of chosen blog."""
    blog = get_object_or_404(Blog, id=blog_id)
    headlines = blog.entry_set.order_by('-pub_date')
    context = {'blog': blog, 'headlines': headlines}
    return render(request, 'query/blog.html', context)

@login_required
def new_blog(request):
    """Add new blog."""
    if request.method != 'POST':
        #No data posted, show empty form.
        form = BlogForm()
    else:
        #Data posted by POST request, process them.
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('query:blog', kwargs={'blog_id': new_blog.id}))
            
    context = {'form': form}
    return render(request, 'query/new_blog.html', context) 

@login_required 
def new_entry(request, blog_id):
    """Add new entry to blog."""
    blog = get_object_or_404(Blog, id=blog_id)
    check_blog_owner(blog, request)    
    
    if request.method != 'POST':
        #No data posted, show empty form.
        form = EntryForm()
        form.helper.layout[0][0] = check_form_edit_or_new('new', form)
    else:
        #Data posted by POST request, process them.
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            new_entry.save()
            return HttpResponseRedirect(reverse('query:blog', args=[blog_id]))
           
    context = {'blog': blog, 'form': form}
    return render(request, 'query/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Blog entry edition."""
    entry = get_object_or_404(Entry, id=entry_id)
    blog = entry.blog
    check_blog_owner(blog, request)    
    
    
    if request.method != 'POST':
        #Initial request, filling the form with actual content of entry data.
        form = EntryForm(instance=entry)
        edit_legend, edit_button = check_form_edit_or_new('edit', form)
        form.helper.layout[0][0] = edit_legend
        form.helper.layout[1][0][0] = edit_button
    else:
        #POST request, data has to be processed.
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('query:blog', args=[blog.id]))
            
    context = {'entry': entry, 'blog': blog, 'form': form}
    return render(request, 'query/edit_entry.html', context)

@login_required
def edit_blog(request, blog_id):
    """Edition of blog informations"""
    blog = get_object_or_404(Blog, id=blog_id)
    check_blog_owner(blog, request)
    
    if request.method != 'POST':
        #Initial request, filling the form with actual content of blog data.
        form = BlogForm(instance=blog)
        edit_legend, edit_button = check_form_blog_edit_or_new('edit', form)
        form.helper.layout[0][0] = edit_legend
        form.helper.layout[1][0][0] = edit_button
    else:
        #POST request, data has to be processed.
        form = BlogForm(instance=blog, data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('query:blog', args=[blog.id]))
            
    context = {'blog': blog, 'form': form}
    return render(request, 'query/edit_blog.html', context)

def check_blog_owner(blog, request):
    """Checks if blog is registered to user."""
    if blog.owner != request.user:
        raise Http404

