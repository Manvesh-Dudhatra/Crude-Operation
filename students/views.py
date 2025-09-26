from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student
from django.template import loader

def addStudent(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        std = request.POST.get("std")
        
        newStudent = Student.objects.create(name = name, email = email, std = std)
        newStudent.save()
        return redirect('display-student')
        


    return render(request, 'add_student.html')

def displayStudent(request):
    
    students = Student.objects.all()
    student1 = Student.objects.filter(id__lt =5).values()
    student2 = Student.objects.values_list('email', 'name')
    # student2 = Student.objects.first()
    
    
    
    context = {
        "students":students,
        "student":student2,
    }

    return render(request, 'display_students.html', context)


def updateStudent(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        # student = get_object_or_404(Student, id=id)
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.std = request.POST.get("std")

        student.save()
        return redirect("display-student")
    return render(request, 'update_student.html', {"students":student})

def deleteStudent(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("display-student")

# def main(request):
#     template = loader.get_templatate("main.html")
#     students = Student.objects.all()
#     context = {
#         "students":students

#     }

#     return HttpResponse(template.render(request, context))


    




