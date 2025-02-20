from django.urls import path
from django.shortcuts import render
from .views import report

urlpatterns = [
    path("reportapi/", report, name="reportapi"),
    path("report/", lambda request: render(request, "report.html"), name="report"),
]
