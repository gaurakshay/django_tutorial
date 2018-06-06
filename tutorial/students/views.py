from django.shortcuts import render

# import the template view.
from django.views.generic import TemplateView


class WelcomeView(TemplateView):
    template_name = 'welcome.html'

