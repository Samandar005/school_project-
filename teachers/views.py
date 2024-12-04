from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teacher-list.html', ctx)

def teacher_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        if first_name and last_name and subject:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject
            )
            return redirect('teachers:teacher_list')
    return render(request, 'teachers/teacher-form.html')


def teacher_detail(request, pk):
    teachers = get_object_or_404(Teacher, pk=pk)
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teacher-detail.html', ctx)

def teacher_delete(request, pk):
    teachers = get_object_or_404(Teacher, pk=pk)
    teachers.delete()
    return redirect('teachers:teacher_list')
