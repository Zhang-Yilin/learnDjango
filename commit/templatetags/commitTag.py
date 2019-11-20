from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Commit

register = template.Library()


@register.simple_tag
def test():
    return "tttt"


@register.simple_tag
def get_commit_num(blog):
    blog_content_type =  ContentType.objects.get_for_model(blog)
    commit_num = Commit.objects.filter(content_type=blog_content_type, object_id=blog.pk).count()
    return commit_num
