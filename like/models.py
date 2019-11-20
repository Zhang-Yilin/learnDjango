from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class LikeCount(models.Model):
    count = models.IntegerField(default=0)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    like_time = models.DateTimeField(auto_now_add=True)


