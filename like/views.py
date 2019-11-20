from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from .models import LikeCount, LikeRecord


def like_change(request):
    content_type = request.GET.get('content_type')
    object_id = int(request.GET.get('object_id'))
    user = request.user
    is_like = request.GET.get('is_like')
    if not user.is_authenticated:
        return error_like(400, '您未登录')


    try:
        content_type = ContentType.objects.get(model=content_type)
        mclass = content_type.model_class()
        model_obj = mclass.objects.get(pk = object_id)
    except ObjectDoesNotExist:
        return error_like(404, '对象不存在')


    if is_like == 'true':
        like_record, created = LikeRecord.objects.get_or_create(content_type=content_type, object_id=object_id,
                                                                user=user)
        if created:
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            like_count.count += 1
            like_count.save()
            return success_like(like_count.count)
        else:
            return error_like(402, '您已点赞')
    else:
        if LikeRecord.objects.filter(content_type=content_type, object_id=object_id,
                                                                user=user).exists():
            record = LikeRecord.objects.filter(content_type=content_type, object_id=object_id, user=user)
            record.delete()
            like_count, created2 = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            if not created2:
                like_count.count -= 1
                like_count.save()
                return success_like(like_count.count)
            else:
                return error_like(404, '数据')
        else:
            return error_like(403, '您未点赞')


def success_like(like_num):
    jsondata = {}
    jsondata['status'] = 'SUCCESS'
    jsondata['like_num'] = like_num
    return JsonResponse(jsondata)


def error_like(code, message):
    jsondata = {}
    jsondata['status'] = 'ERROR'
    jsondata['code'] = code
    jsondata['meaasge'] =message
    return JsonResponse(jsondata)



