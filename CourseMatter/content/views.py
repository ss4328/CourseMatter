from django.views import generic
from .models import Content
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# from .forms import ContentForm

class ContentList(generic.ListView):
    queryset = Content.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class ContentDetail(generic.DetailView):
    model = Content
    template_name = 'content_detail.html'

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

'''
Returns view with all posts for a single tag
'''
class TagListView(ListView):
    template_name = "tag_contents.html"

    def get_queryset(self):
        return Content.objects.filter(tags__slug=self.kwargs.get("tag_slug")).all()
