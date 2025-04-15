from django.db import models

"""CREATE TABLE posts(id serial primary key autoincrement, title varchar(256), content varchar(856), rate int);"""
"""a
ll objects - SELECT * FROM post ===> Post.objects.all
filtred objects - SELECT * FROM post WHERE title = ILIKE('title') ===> Post.objects.filter(title_icontains="title")
one object -SELECT * FROM post WHERE id = 1==> Post.objects.get(id=1)
"""

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"
    

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"





class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=356)
    content = models.CharField(max_length=856)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    Tag = models.ManyToManyField(Tag)

def __str__(self):
    return f" {self.title} {self.content} self.id"