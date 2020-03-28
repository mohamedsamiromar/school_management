from django import forms

from apps.entry_app.models import Student, Subject, Teacher, Classes, StudentTcs, TeacherClassSubject


class StudentForm(forms.ModelForm):
    class_name = forms.CharField()
    class Meta:
        model = Student
        fields = ['name', 'study_year', 'birthday', 'class_name']


# class SubjectRelationForm(forms.ModelForm):
#      teacher_name = forms.CharField()
#      student_name = forms.CharField()
#      subject_name = forms.CharField()
#      class Meta:
#          model = SubjectRelation
#          fields = ['subject_name', 'take_exam', 'grade', 'teacher_name', 'student_name']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'max_grade']

class TeacherForm(forms.ModelForm):
    user_name = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = Teacher
        fields = ['name', 'salary', 'address1', 'user_name', 'password']

class ClassesForm(forms.ModelForm):
    floor_index = forms.CharField()
    class Meta:
        model = Classes
        fields = ['name', 'floor_index']


class TeacherClassSubjectForm(forms.ModelForm):
        teacher_name = forms.CharField()
        class_name = forms.CharField()
        subject_name = forms.CharField()

        class Meta:
            model = TeacherClassSubject
            fields = ['subject_name', 'teacher_name', 'class_name']

class StudentTcsForm(forms.ModelForm):
    student_name = forms.CharField()
    subject_name = forms.CharField()
    teacher_name = forms.CharField()
    class_name = forms.CharField()


    class Meta:
        model = StudentTcs
        fields = ['grade']