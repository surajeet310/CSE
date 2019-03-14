from django.shortcuts import render
from .models import Notices
from details.models import Semester
from .models import Slide
from .models import Event


def home(request):
        notice = Notices.objects.order_by('-notice_upload_time').all()
        semester = Semester.objects.all()
        slide = Slide.objects.all()
        event = Event.objects.all()
        context = {
            'notice': notice,
            'semester': semester,
            'slide': slide,
            'event': event
        }
        return render(request, "../templates/notice/home.html", context)


def filter_query(request):
    if request.method == 'POST':
        sid = request.POST.get('sem')

        notice = Notices.objects.filter(sem_id=sid).order_by('-notice_upload_time').all()
        semester = Semester.objects.all()
        context = {
            'notice': notice,
            'semester': semester
        }

        return render(request, "../templates/notice/home.html", context)


def output_notice(request, notice_id):
    file = Notices.objects.get(notice_id=notice_id)
    return render(request, "../templates/notice/noticeOutput.html", {'file': file})



