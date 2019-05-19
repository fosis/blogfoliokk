from django.contrib.auth.models import User
from query.models import Blog, Entry, Author

blog = Blog.objects.all()
ath = Author.objects.all()
ur = User.objects.all()

for ar in User.objects.all():
    Author.objects.create(owner=ar)

for b in blog:
    for a in ath:
        if a.owner == b.owner:
            Blog.objects.filter(owner=b.owner).update(author=a)
     
nullnn = Author.objects.filter(nickname='')
for nn in nullnn:
    nn.nickname = str(nn.owner) + 'query'
    nn.save()
        
nauthors = Author.objects.filter(owner=None)
for na in nauthors:
    na.owner = User.objects.get(username='admin')
    na.save()
        
for b in blog:
    for a in ath:
        if a.owner == b.owner:
            ba = Author.objects.get(pk=a.pk)
            nb = Blog.objects.filter(owner=b.owner)
            for bg in nb:
                blogname = bg.id
                ba.blogs.add(blogname)
                ba.save()


>>> author = Author.objects.filter(owner__in=User.objects.filter(username='admin'))
