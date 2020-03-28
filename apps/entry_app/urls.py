from django.urls import path
from apps.entry_app import views

urlpatterns = [
    path('student', views.student, name='student'),
    path('subject', views.subject, name='subject'),
    path('teacher', views.teacher, name='teacher'),
    path('classes', views.classes, name='classes'),
    # path('relation', views.subject_relation, name='subject_relation'),
    path('tcs', views.teacher_subject_relation, name='teacher_subject_relation'),
    path('sts', views.student_degree_subject, name='StudentTcs')
]
