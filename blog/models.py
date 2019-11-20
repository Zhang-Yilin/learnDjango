from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

class BlogType(models.Model):
    type_name = models.CharField(max_length = 20)
    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50, default="Null")
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default="1")
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, related_name="blog_t")
    read_num = models.IntegerField(default=0)
    
    def __str__(self):
        return "blog name: "+self.title

    class Meta:
        ordering = ["-created_time", "-last_update_time",]

class ReadList(models.Model):
    read_time = models.DateTimeField(auto_now_add=True)
    reader = models.ForeignKey(User, on_delete=models.DO_NOTHING, default="1")
    read_blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)






