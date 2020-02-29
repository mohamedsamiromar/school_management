from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.entry_app.form import StudentForm, TeacherForm, ClassesForm, SubjectForm, SubjectRelationForm
from apps.entry_app.models import Student, Subject, Classes, Teacher, SubjectRelation


@login_required
def student(request):
    if request.method == 'GET':
        model = {}
        model['students'] = Student.objects.all()
        if 'student_id' in request.GET:
            student_id = request.GET.get("student_id")
            student = Student.objects.get(pk=student_id)
            model['active_student'] = student

        return render(request, 'entries/student.html', model)

    elif request.method == 'POST':
        if 'id' in request.POST:
            # Handle update existing student
            id = request.POST.get('id')
            student = Student.objects.get(pk=id)
            student_form = StudentForm(request.POST, instance=student)
            if student_form.is_valid():
                student_form.save()
            return render(request, 'entries/student.html', {'form': student_form, 'students': Student.objects.all()})
        else:
            # Handle create new student
            student_form = StudentForm(request.POST)
            if student_form.is_valid():
                # Convert student form to student model
                student = student_form.save(commit=False)
                class_name = student_form.cleaned_data['class_name']
                student.student_class = Classes.objects.filter(name=class_name).first()
                student.save()
            students = Student.objects.all()
            return render(request, 'entries/student.html', {'form': student_form, 'students': students})
    # elif request.method == 'PUT':
    #     id = request.PUT.get('id')
    #     student = Student.objects.get(pk=id)
    #     del request.PUT['id']
    #     student_form = StudentForm(request.PUT, instance=student)
    #     if student_form.is_valid():
    #         student_form.save()
    #     return render(request, 'student.html', {'form': student_form, 'students': student})


def subject(request):
    if request.method == 'GET':
        model = {}
        model['subjects'] = Subject.objects.all()
        if 'subject_id' in request.GET:
            subject_id = request.GET.get("subject_id")
            subject = Subject.objects.get(pk=subject_id)
            model['active_subject'] = subject
        return render(request, 'entries/subject.html', model)
    elif request.method == 'POST':
        if 'id' in request.POST:
            id = request.POST.get('id')
            subject = Subject.objects.get(pk=id)
            subject_form = SubjectForm(request.POST, instance=subject)
            if subject_form.is_valid():
                subject_form.save()
            return render(request, 'entries/subject.html', {'form': subject_form, 'subjects': Subject.objects.all()})
        else:
            subject_form = SubjectForm(request.POST)
            if subject_form.is_valid():
                subject_form.save()
            subjects = Subject.objects.all()
            return render(request, 'entries/subject.html', {'form': subject_form, 'subjects': subjects})


def subject_relation(request):
    if request.method == 'GET':
        model = {}
        model['subjects'] = SubjectRelation.objects.all()
        if 'rel_id' in request.GET:
            rel_id = request.GET.get("rel_id")
            relation = SubjectRelation.objects.get(pk=rel_id)
            model['active_subject_relation'] = relation
        return render(request, 'entries/subjectrelation.html', model)

    elif request.method == 'POST':
        rel_form = SubjectRelationForm(request.POST)
        if 'id' in request.POST:
            id = request.POST.get('id')
            relation = SubjectRelation.objects.get(pk=id)
            rel_form = SubjectRelationForm(request.POST, instance=relation)

        if rel_form.is_valid():
            rel = rel_form.save(commit=False)

            teacher_name = rel_form.cleaned_data['teacher_name']
            rel.teacher = Teacher.objects.filter(name=teacher_name).first()

            student_name = rel_form.cleaned_data['student_name']
            rel.student = Student.objects.filter(name=student_name).first()

            subject_name = rel_form.cleaned_data['subject_name']
            rel.subject = Subject.objects.filter(subject_name=subject_name).first()

            rel.save()


        subjects = SubjectRelation.objects.all()
        return render(request, 'entries/subjectrelation.html', {'form': rel_form, 'subjects': subjects})


def teacher(request):
    if request.method == 'GET':
        model = {}
        model['teachers'] = Teacher.objects.all()
        if 'teacher_id' in request.GET:
            teacher_id = request.GET.get("teacher_id")
            teacher = Teacher.objects.get(pk=teacher_id)
            model['active_teacher'] = teacher
        return render(request, 'entries/teacher.html', model)

    elif request.method == 'POST':
        if 'id' in request.POST:
            id = request.POST.get('id')
            teacher = Teacher.objects.get(pk=id)
            teacher_form = TeacherForm(request.POST, instance=teacher)
            if teacher_form.is_valid():
                teacher_form.save()
            return render(request, 'entries/teacher.html', {'form': teacher_form, 'teachers': Teacher.objects.all()})



        else:
            teacher_form = TeacherForm(request.POST)
            if teacher_form.is_valid():
                teacher_form.save()
                teachers = Teacher.objects.all()
                return render(request, 'entries/teacher.html', {'form': teacher_form, 'teachers': teachers})


def classes(request):
    if request.method == 'GET':
        model = {}
        model['classes'] = Classes.objects.all()
        if 'classes_id' in request.GET:
            classes_id = request.GET.get()
            _class = Classes.objects.get(pk=classes_id)
            model['active_class'] = _class
        return render(request, 'entries/classes.html', model)

    elif request.method == 'POST':
        if 'id' in request.POST:
            id = request.POST.get('id')
            current_class = Classes.objects.get(pk=id)
            classes_form = ClassesForm(request.POST, instance=current_class)
            if classes_form.is_valid():
                classes_form.save()
            return render(request, 'entries/classes.html', {'form': classes_form, 'classess': Classes.objects.all()})


        else:
            classes_form = ClassesForm(request.POST)
            if classes_form.is_valid():
                classes_form.save()
                classes = Classes.objects.all()
                return render(request, 'entries/classes.html', {'form': classes_form, 'classess': classes})

