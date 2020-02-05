
from django.contrib import admin
from django.urls import path
from apps.report_app import views


urlpatterns = [
    path('students/simple', views.simple_report, name='students_simple'),
    path('students/grade', views.grade_report, name='grade_report'),
]