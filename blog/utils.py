from .models import ReadList
from django.utils import timezone
from django.db.models import Count
import datetime

def get_hot_blog():
    now = timezone.now()
    hot_blog = ReadList.objects.filter(read_time__day=now.day).values("read_blog","read_blog__title").annotate(count = Count('read_blog'))\
        .order_by("-count")
    return hot_blog[:7]