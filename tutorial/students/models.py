from django.db import models

# Create your models here.


class Department(models.Model):
    """
    This model will store the details about our department.
    Primary key for this model is department code.
    """
    class Meta:
        db_table = "departments"
        ordering = ['d_name']

    d_name = models.CharField(max_length=200, verbose_name="Department Name")
    d_code = models.CharField(max_length=5, primary_key=True, verbose_name="Department Code")
    d_chair = models.CharField(max_length=200, verbose_name="Department Chair")

    def __str__(self):
        """
        String representation of the department.
        This will be used mainly when we print
        a department object.
        """
        return self.d_name


class Course(models.Model):
    """
    This model will store the details about courses
    present in the sytem.
    Primary key for this model is a combination of
    course code and department code (compound key)
    """
    class Meta:
        """
        Compound key is defined by the keyword unique_together
        """
        db_table = 'courses'
        unique_together = (('department', 'c_code'), )

    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Department Name")
    c_code = models.IntegerField(verbose_name="Course Code")
    c_name = models.CharField(max_length=200, verbose_name="Course Name")
    c_seats = models.IntegerField(verbose_name="Number of Seats")
    c_desc = models.TextField(blank=True, verbose_name="Course Description")

    def __str__(self):
        """
        String representation of the object.
        """
        return self.c_name


class Student(models.Model):
    """
    This model will store students' details.
    Primary key will be the students' id.
    """

    class Meta:
        db_table = 'students'
        ordering = ['s_id']

    s_id = models.IntegerField(primary_key=True, verbose_name="Student ID")
    s_first_name = models.CharField(max_length=200, verbose_name="First Name")
    s_last_name = models.CharField(max_length=200, verbose_name="Last Name")
    s_pic = models.ImageField(upload_to='student_pics', blank=True, verbose_name="Student's pic")
    course = models.ManyToManyField(Course, blank=True, verbose_name="Courses")

    def __str__(self):
        """
        String representation of the student object.
        """
        return "{0} {1}".format(self.s_first_name, self.s_last_name)


