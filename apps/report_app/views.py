from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from apps.school_app.models import Student, SubjectRelation


def simple_report(request):
    class_name = request.GET.get('class_name', '')
    class_students = []
    if class_name is not '':
        class_students = Student.objects.filter(student_class__name=class_name).order_by('name')
    return render(request, "reports/students_report_simple.html", {'students': class_students, 'class_name': class_name})


def grade_report(request):
    class_name = request.GET.get('class_name', '')
    students_class_sum = []
    if class_name is not '':
        #class_students = Student.objects.filter(student_class__name=class_name).order_by('name')
        students_class_sum = SubjectRelation.objects.filter(student__student_class__name=class_name)\
            .values('student').annotate(sum_degrees=Sum('grade'))
        for itm in students_class_sum: # item = {student: 22, sum_degree=50}
            itm['student'] = Student.objects.get(pk=itm['student'])

    return render(request, "reports/students_report_grade.html", {'students': students_class_sum, 'class_name': class_name})