from django.views.generic import ListView
from .models import Page


class HomePageView(ListView):
    model = Page
    template_name = 'home.html'
    context_object_name = 'all_pages_list'

class AboutPageView(ListView):
    template_name = 'about.html'


