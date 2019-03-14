from django.shortcuts import render
from details.models import Batch
from .models import Alumini


def alumini_search(request):
    studentBatch = Batch.objects.all()
    context1 = {'studentBatch': studentBatch}
    return render(request, "../templates/alumini/alumini_search.html", context1)


def alumini_search_batch(request):
    studentBatch = Batch.objects.all()
    return render(request, "../templates/alumini/BatchView.html", {'studentBatch': studentBatch})


def name_search(request):
    context = {}
    if request.method == 'POST':
        Fname = request.POST.get('fname')
        Lname = request.POST.get('lname')
        Bid = request.POST.get('batch')
        queryResults = Alumini.objects.filter(First_name=Fname, Last_name=Lname, batch_id=Bid).all()
        context.update({'queryResults': queryResults})
        return render(request, "../templates/alumini/search_result.html", context)
    else:
        context = {}
        return render(request, "../templates/alumini/ErrorPage.html", context)


def roll_search(request):
    context2 = {}
    if request.method == 'POST':
        Roll = request.POST.get('roll')
        Number = request.POST.get('no')
        bid = request.POST.get('batch')
        queryResults = Alumini.objects.filter(roll=Roll, number=Number, batch_id=bid).all()
        context2.update({'queryResults': queryResults})
        return render(request, "../templates/alumini/search_result.html", context2)
    else:
        context2 = {}
        return render(request, "../templates/alumini/ErrorPage.html", context2)


def BatchView(request):
    context = {}
    if request.method == 'POST':
        bid = request.POST.get('batch_search')
        queryResults = Alumini.objects.filter(batch_id=bid).all()
        context.update({'queryResults': queryResults})
        return render(request, "../templates/alumini/search_result.html", context)
    else:
        context = {}
        return render(request, "../templates/alumini/ErrorPage.html", context)
