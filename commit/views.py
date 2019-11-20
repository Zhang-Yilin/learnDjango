from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from .models import Commit
from .form import CommitForm

def commit_submit(request):
    """
    refer = request.META.get("HTTP_REFERER", "/home")

    user = request.user
    text = request.POST.get("text")
    text_detect = text.strip()
    if text_detect == "":
        return render(request, "error.html", {"message": "评论为空", "redirect": refer})
    object_id = int(request.POST.get("object_id",""))
    typem = request.POST.get("content_type","")
    model_class = ContentType.objects.get(model=typem).model_class()
    model_obj = model_class.objects.get(pk = object_id)

    commit = Commit()
    commit.user = user
    commit.text = text
    commit.commit_time = now()
    commit.content_object = model_obj
    commit.save()
    return redirect(refer)
    """
    refer = request.META.get("HTTP_REFERER", "/home")
    commit_form = CommitForm(request.POST, user=request.user)
    if commit_form.is_valid():
        commit = Commit()
        commit.user = request.user
        commit.text = commit_form.cleaned_data['text']
        commit.content_object = commit_form.cleaned_data['content_object']
        parent = commit_form.cleaned_data['parent']
        if not parent is None:
            commit.root = parent.root if not parent.root is None else parent
            commit.parent = parent
            commit.reply_to = parent.user
        commit.save()

        data={}
        data['statue'] = 'SUCCESS'
        data['username'] = commit.user.username
        data['created_time'] = commit.commit_time.timestamp()
        data['text'] = commit.text
        if not parent is None:
            data['reply_to'] = commit.reply_to.username
        else:
            data['reply_to'] = ""
        data['root_pk'] = commit.root.pk if not commit.root is None else ''
        data['pk'] = commit.pk

    else:
        data = {}
        data['statue'] = 'ERROR'
    return JsonResponse(data)


