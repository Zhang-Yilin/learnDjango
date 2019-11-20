from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.
class Commit(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()
    commit_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    root = models.ForeignKey('self', related_name='rootc', null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='parentc', null=True, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(User, related_name='replies', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["commit_time"]


