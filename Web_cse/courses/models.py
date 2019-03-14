from django.db import models
from details.models import Semester


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_title = models.CharField(blank=False, max_length=100)
    course_file = models.FileField(blank=False)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_title
