from django.urls import path
from . import views

urlpatterns = [
    path('commit_submit', views.commit_submit, name="commit_submit"),
]
