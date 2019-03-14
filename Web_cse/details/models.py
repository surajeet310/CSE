from django.db import models


class Semester(models.Model):
    sem_id = models.AutoField(primary_key=True)
    sem = models.CharField(max_length=4)

    def __str__(self):
        return self.sem


class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    batch = models.CharField(max_length=10)

    def __str__(self):
        return self.batch
