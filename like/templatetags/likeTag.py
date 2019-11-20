from django import template
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ..models import LikeCount, LikeRecord

register = template.Library()


@register.simple_tag
def blog_type(blog):
    blog_content_type = ContentType.objects.get_for_model(blog)
    return blog_content_type.model

@register.simple_tag
def get_content_type(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return content_type.model

@register.simple_tag
def get_like_num(blog):
    blog_content_type =  ContentType.objects.get_for_model(blog)
    commit_num = LikeCount.objects.filter(content_type=blog_content_type, object_id=blog.pk).count()
    return commit_num


@register.simple_tag
def like_status(obj, user):
    if not user.is_authenticated:
        like_status = ''
        return like_status
    else:
        obj_content_type = ContentType.objects.get_for_model(obj)
        try:
            like_record = LikeRecord.objects.get(content_type=obj_content_type, object_id=obj.pk)
            like_status = 'active'
        except  ObjectDoesNotExist:
            like_status = ''
        return like_status


@register.simple_tag
def like_num(obj):
    obj_content_type = ContentType.objects.get_for_model(obj)
    try:
        like_record = LikeCount.objects.get(content_type=obj_content_type, object_id=obj.pk)
        count = like_record.count
    except ObjectDoesNotExist:
        count = 0
    return count

