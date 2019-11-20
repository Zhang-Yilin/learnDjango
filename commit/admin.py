from django.contrib import admin
from .models import Commit
# Register your models here.


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ('content_type',"object_id",'text',"commit_time", "user", "id", 'parent', 'pk')