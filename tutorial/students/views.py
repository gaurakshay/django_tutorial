from django.shortcuts import render

# import the template view.
from django.views.generic import TemplateView, ListView, DetailView

# import department model
from students.models import Department


class WelcomeView(TemplateView):
    """
    This is our welcome screen. Utilizes a
    template view.
    """
    template_name = 'welcome.html'


class DeptListView(ListView):
    """
    This class handles the list view for
    department model. Utilizes the list view
    """
    template_name = 'dept-list.html'
    model = Department
    context_object_name = 'depts'


class DeptDetailView(DetailView):
    """
    This is the detail view of the class.
    Uses the default detail view provided
    by Django Framework.
    """
    template_name = 'dept-details.html'
    model = Department
    context_object_name = 'dept'

