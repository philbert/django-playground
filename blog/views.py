""" a new view for a new day """
from django.views.generic import ListView

from blog.models import Entry


class HomeView(ListView):
    """ not home but actually /blog/ """
    template_name = 'blog.html'
    queryset = Entry.objects.order_by('-created_at')
