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

    d_name = models.CharField(max_length=200)
    d_code = models.CharField(max_length=5, primary_key=True)
    d_chair = models.CharField(max_length=200)

    def __unicode__(self):
        """
        String representation of the department.
        This will be used mainly when we print
        a department object.
        """
        return self.d_name


#class Courses(models.Model):
#    """
#    This model will store the details about courses
#    present in the sytem.
#    Primary key for this model is a combination of
#    course code and department code (compound key)
#    """
#    class Meta:
#        db_table = 'courses'
#        unique_together = (('c_d_code', 'c_code'), )
#
#    c_d_code = models.ForeignKey(Department)
#    c_code = models.IntegerField()
#    c_name = models.CharField(max_length=200)
#    c_seats = models.IntegerField()
#    c_desc = models.TextField(blank=True)
#
#    def __unicode__(self):
#        """
#        String representation of the object.
#        """
#        return self.c_name
#
#
#class Students(models.Model):
#    """
#    This model will store our student's details.
#    Primary key will be the student's id.
#    """
#
#    class Meta:
#        db_table = 'students'
#        ordering = ['student_id']
#
#    s_id = IntegerField(primary_key=True)
#    s_first_name = CharField(max_length=200)
#    s_last_name = CharField(max_length=200)
#    s_pic = ImageField(upload_to='student_pics', blank=True)
#    courses = ManyToManyField(Course)


