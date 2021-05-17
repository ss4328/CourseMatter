from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import AddContentView, UpdateContentView

urlpatterns = [
    path('', views.ContentList.as_view(), name='index'),
    path('<slug:slug>/', views.ContentDetail.as_view(), name='content_detail'),
    path('content_detail/<slug:slug>/', views.ContentDetail.as_view(), name='content_detail'),
    path('tags/<slug:tag_slug>/', views.TagListView.as_view(), name='content_by_tag'),
    path('add_content', AddContentView.as_view(), name="add_content"),
    path('content/edit/<slug:slug>', UpdateContentView.as_view(), name="edit_content")
]