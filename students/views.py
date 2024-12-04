from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def home(request):
    return render(request, 'index.html')

def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student-list.html', ctx)

def student_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        if first_name and last_name and age and email:
            Student.objects.create(
                first_name=first_name,
                last_name= last_name,
                age=age,
                email=email
            )
            return redirect('students:student_list')
    return render(request, 'students/student-form.html')

def student_detail(request, pk):
    students = get_object_or_404(Student, pk=pk)
    ctx = {'students': students}
    return render(request, 'students/student-detail.html', ctx)

def student_delete(request, pk):
    students = get_object_or_404(Student, pk=pk)
    students.delete()
    return redirect('students:student_list')
























