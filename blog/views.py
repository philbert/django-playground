""" a new view for a new day """
from django.views.generic import ListView, CreateView

from blog.forms import CommentForm
from blog.models import Entry


class HomeView(ListView):
    """ not home but actually /blog/ """
    template_name = 'blog.html'
    queryset = Entry.objects.order_by('-created_at')

class EntryDetail(CreateView):
    """ a new day a new adventure """
    model = Entry
    template_name = 'blog/entry_detail.html'
    form_class = CommentForm

    def get_form_kwargs(self):
        """ get key word arguments """
        kwargs = super().get_form_kwargs()
        kwargs['entry'] = self.get_object()
        return kwargs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['entry'] = self.get_object()
        return data
