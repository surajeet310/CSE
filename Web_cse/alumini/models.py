from django.db import models
from details.models import Batch


class Alumini(models.Model):
    alumini_id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=50, blank=False)
    Last_name = models.CharField(max_length=30, blank=False)
    roll = models.IntegerField(blank=False)
    number = models.IntegerField(blank=False)
    batch_id = models.ForeignKey(Batch, on_delete=models.CASCADE)
    pass_out_year = models.CharField(max_length=10, blank=False)
    cgpa = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1}".format(self.First_name, self.Last_name)
