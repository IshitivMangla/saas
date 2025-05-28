from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home(request):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    context = {
        "page_head" : "Hello World!",
        "total_visit_count" : qs.count(),
        "page_visit_count" : page_qs.count()
    }
    PageVisit.objects.create(path = request.path)
    return render(request, "home.html", context)

def hello(request):
    return HttpResponse("<h1>Hello</h1>")
