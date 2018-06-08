from django.forms import ModelForm

# Import models
from students.models import Student


class StudentForm(ModelForm):
    """
    This is the modelfrom for the student.
    """
    class Meta:
        model = Student
        fields = ['s_id', 's_first_name', 's_last_name', 's_pic', 'course']
