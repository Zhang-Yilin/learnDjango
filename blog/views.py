from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Count, ObjectDoesNotExist
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from commit.models import Commit
from commit.form import CommitForm
from like.models import LikeCount, LikeRecord
from .models import BlogType, Blog, ReadList
from mysite.form import LoginForm

def get_common_data(blog_list, request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 4)
    page_of_blogs = paginator.get_page(page_num)
    page_range = list(range(max(1,int(page_of_blogs.number)-2),page_of_blogs.number)) + \
                 list(range(page_of_blogs.number, min(int(page_of_blogs.number)+2, paginator.num_pages)+1))
    context = {}
    context['types'] = BlogType.objects.annotate(blog_count=Count("blog_t"))
    context['page_range'] = page_range
    context['blog_date'] = Blog.objects.dates("created_time", "month", order="DESC")
    blog_dict = {}
    for i in page_of_blogs.object_list:
        num = len(ReadList.objects.filter(read_blog=i))
        blog_dict[i] = num
    context['record'] = blog_dict
    return context


def blog_list(request):
    blog_to_page = Blog.objects.all()
    context = get_common_data(blog_to_page, request)
    response = render(request, "blog/blog_list.html", context)
    return response

def blog_detail(request, blog_id):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_id)
    if not request.COOKIES.get('read_%s_time' % blog.pk) == 'true':
        read_record = ReadList()
        read_record.read_time = datetime.now()
        read_record.read_blog = blog
        # read_record.reader=
        read_record.save()

    blog_content_type = ContentType.objects.get_for_model(blog)
    commit = Commit.objects.filter(content_type=blog_content_type, object_id=blog.pk, parent=None).order_by('-commit_time')
    commit_count = Commit.objects.filter(content_type=blog_content_type, object_id=blog.pk).count()

    read_num = ReadList.objects.filter(read_blog=blog).count()
    try:
        like_count = LikeCount.objects.get(content_type=blog_content_type, object_id=blog.pk)
        like_num = like_count.count
    except ObjectDoesNotExist:
        like_num = 0



    context['blog'] = get_object_or_404(Blog, pk=blog_id)
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt= blog.created_time).first()
    context['read_num'] = read_num
    context['commits'] = commit
    context['commit_form'] = CommitForm(initial={'content_type':str(blog_content_type), 'object_id':blog_id,
                                                 "reply_comment_id": 0})
    context['commit_num'] = commit_count
    context['like_num'] = like_num
    context['login_form'] = LoginForm()
    context['user'] = request.user
    response = render(request, "blog/blog_detail.html", context)
    response.set_cookie('read_%s_time' % blog.pk, 'true')
    return response


def blog_with_type(request, type_id):
    context = {}
    type = get_object_or_404(BlogType, pk = type_id)
    context['blogs'] = Blog.objects.filter(blog_type=type)
    context['type'] = type
    response = render(request, "blog/blog_with_type.html", context)
    return response

def blog_date(request, month, year):
    blog_to_date = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = get_common_data(blog_to_date, request)
    context['year'] = year
    context['month'] = month
    response = render(request, "blog/blog_date.html", context)
    return response




