from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('list/', views.blog_list, name='blog_list'),
    path('type/<int:type_id>', views.blog_with_type, name="blog_with_type"),
    path('date/<int:year>/<int:month>', views.blog_date, name="blog_date"),
]
