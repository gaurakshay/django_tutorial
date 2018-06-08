from django.shortcuts import render

# import the generic views.
from django.views.generic import TemplateView, ListView, DetailView, CreateView

# import models
from students.models import Department, Student

# import forms
from students.forms import StudentForm

#import reverse lazy
from django.urls import reverse_lazy

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


class StudentListView(ListView):
    """
    Return list of students in the system.
    """
    template_name = 'stud-list.html'
    model = Student
    context_object_name = 'students'


class StudentDetailView(DetailView):
    """
    This class utilizes the default class
    based view provided by Django framework to
    display the details of a student in the system
    """
    template_name = 'stud-details.html'
    model = Student
    context_object_name = 'student'


class StudentAddView(CreateView):
    """
    This class utilizes the default class based
    view provided by Django framework to add submitted
    data to backend database.
    """
    template_name = 'stud-edit.html'
    model = Student
    form_class = StudentForm
    # Use reverse lazy to create the url for our list view
    # the parameter is the named url in our urls.py file.
    # success_url = reverse_lazy('stud_list')

