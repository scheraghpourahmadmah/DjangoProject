from django.shortcuts import render

# Create your views here.(set up all business logic,htttp request and responses)

from django.http import HttpResponse

def homepage(request):
    return HttpResponse('This is the homepage')

def register(request):
    return HttpResponse('This is the registration page')

def report_view(request):
    reports = Report.objects.prefetch_related("pictures").all()
    return render(request, "report.html", {"reports": reports})