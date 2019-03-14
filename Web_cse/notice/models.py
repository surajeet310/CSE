from django.db import models
from details.models import Semester


class Notices(models.Model):
    notice_id = models.AutoField(primary_key=True)
    notice_content = models.CharField(max_length=1000, blank=False)
    noticeFile = models.FileField(blank=False)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    notice_upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notice_content


class Slide(models.Model):
    slideId = models.AutoField(primary_key=True)
    slideCaption = models.CharField(blank=False, default='Picture', max_length=30)
    slidePic = models.FileField(blank=False)

    def __str__(self):
        return self.slideCaption


class Logo(models.Model):
    logo_pic = models.FileField(blank=False)


class Event(models.Model):
    event_content = models.CharField(max_length=1000, blank=False)
    event_header = models.CharField(max_length=50, blank=False)
    event_img = models.FileField(blank=False)
    event_id = models.AutoField(primary_key=True)
    event_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_header
