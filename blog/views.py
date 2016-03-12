""" a new view for a new day """
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    """ not home but actually /blog/ """
    template_name = 'blog.html'
