from django.shortcuts import render, redirect, reverse
from blog.models import ReadList
from django.db.models import Count
from django.db.models.functions import ExtractDay, ExtractMonth
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib import auth
from django.contrib.auth.models import User
import datetime
from time import strftime, asctime
from blog.utils import get_hot_blog
from .form import LoginForm, RegisterForm

def getSevenday():
  today=datetime.date.today()
  oneday=datetime.timedelta(days=7)
  sevenday=today-oneday
  return sevenday


def home(request):
    content = {}
    read_num = ReadList.objects.filter(read_time__gte= getSevenday()).\
    extra(select={'day':"strftime('%%Y-%%m-%%d',read_time)"}).values("day").annotate(Count=Count("id"))
    hot_blog_today = cache.get("hot_blog_today")
    if hot_blog_today is None:
        hot_blog_today = get_hot_blog()
        cache.set("hot_blog_today", hot_blog_today, 3600)
    date= [i['day'] for i in list(read_num)]
    read_num = [i['Count'] for i in list(read_num)]
    content['date'] = date
    content['read_num'] = read_num
    content['hot_blogs'] = get_hot_blog()
    response = render(request, "home.html", content)
    return response

