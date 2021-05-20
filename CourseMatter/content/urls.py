from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import AddContentView, UpdateContentView, DeleteContentView, AuthorContentListView, HomeList
from .views import CourseContentView, AddCourseView, UpdateCourseView, DeleteCourseView

urlpatterns = [
    path('', views.HomeList.as_view(), name='index'),
    path('<slug:slug>/', views.ContentDetail.as_view(), name='content_detail'),
    path('tags/<slug:tag_slug>/', views.TagListView.as_view(), name='content_by_tag'),

    path('content/add', AddContentView.as_view(), name="add_content"),
    path('content/edit/<slug:slug>', UpdateContentView.as_view(), name="edit_content"),
    path('content/delete/<slug:slug>', DeleteContentView.as_view(), name="delete_content"),
    path('content_detail/<slug:slug>/', views.ContentDetail.as_view(), name='content_detail'),

    path('course/add', AddCourseView.as_view(), name="add_course"),
    path('course/edit/<slug:slug>', UpdateCourseView.as_view(), name="edit_course"),
    path('course/delete/<slug:slug>', DeleteCourseView.as_view(), name="delete_course"),
    path('course_detail/<slug:course_slug>/', views.CourseContentView.as_view(), name='course_detail'),

    path('content/author/<int:author_id>', views.AuthorContentListView.as_view(), name='content_by_author'),

]


#todo:
#<a href="{% url 'subscribe' user=article.author.id %}">