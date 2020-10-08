from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    """
        Post data model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
            ordering: base on created_on field, -* means decreasing order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
            "Official" representation of the object. It will be used by django for different 
            purposes (administration for ex)
        """
        return self.title