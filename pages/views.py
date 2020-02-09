
# Create your views here.
from django.views.generic import TemplateView  # new


class HomePageView(TemplateView):
    template_name = 'home.html'
