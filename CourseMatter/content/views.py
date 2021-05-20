from django.views import generic
from .models import Content, Course
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
# from .forms import ContentForm
from django.urls import reverse_lazy
from urllib import request
from django.shortcuts import render
from taggit.models import Tag


'''
C(-RUD) for content
'''


class TagListView(ListView):
    template_name = "tag_contents.html"

    def get_queryset(self):
        return Content.objects.filter(tags__slug=self.kwargs.get("tag_slug")).all()


class AuthorContentListView(ListView):
    template_name = "user_contents.html"

    def get_queryset(self):
        return Course.objects.filter(author=self.kwargs.get("author_id")).all()


class HomeList(TemplateView):
    # queryset = Content.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HomeList, self).get_context_data(**kwargs)
        context['contents'] = Content.objects.filter(status=1).order_by('-created_on')
        context['tags'] = Tag.objects.all()
        context['courses'] = Course.objects.all()
        print(context)
        return context


class ContentDetail(DetailView):
    model = Content
    template_name = 'content_detail.html'


'''
RUD(C-) for Content 
'''


class AddContentView(CreateView):
    model = Content
    # form_class = ContentForm
    template_name = 'add_content.html'
    fields = '__all__'


class UpdateContentView(UpdateView):
    model = Content
    # form_class = ContentForm
    template_name = 'update_content.html'
    fields = '__all__'


class DeleteContentView(DeleteView):
    model = Content
    template_name = 'delete_content.html'
    success_url = reverse_lazy('login')




'''
CRUD for Course
'''


class AddCourseView(CreateView):
    model = Course
    # form_class = ContentForm
    template_name = 'add_content.html'
    fields = '__all__'


class CourseContentView(ListView):
    template_name = "course_detail.html"

    def get_queryset(self):
        return Content.objects.filter(course__slug=self.kwargs.get("course_slug")).all()


class UpdateCourseView(UpdateView):
    model = Course
    # form_class = ContentForm
    template_name = 'update_content.html'
    fields = '__all__'


class DeleteCourseView(DeleteView):
    model = Course
    template_name = 'delete_content.html'
    success_url = reverse_lazy('login')
