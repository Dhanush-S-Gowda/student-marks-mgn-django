from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
def home(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        std_id = data.get("std_id")
        sub1_marks = float(data.get("sub1_marks"))
        sub2_marks = float(data.get("sub2_marks"))
        sub3_marks = float(data.get("sub3_marks"))
        sub4_marks = float(data.get("sub4_marks"))
        sub5_marks = float(data.get("sub5_marks"))
        percentage = (sub1_marks+sub2_marks+sub3_marks+sub4_marks+sub5_marks)/5
        percentage = float(f'{percentage:.2f}')
        student = Student.objects.create(name=name,std_id=std_id,sub1_marks=sub1_marks,sub2_marks=sub2_marks,sub3_marks=sub3_marks,sub4_marks=sub4_marks, sub5_marks=sub5_marks, percentage=percentage)
        student.save()
        return redirect('/')
    
    student = Student.objects.all()
    
    return render(request, "index.html", context={"students": student})

def delete_form(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def update_form(request, id):
    up_student = Student.objects.get(id = id)
    all_student = Student.objects.all()
    context = {'update_info': up_student, "students": all_student}
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        std_id = data.get("std_id")
        sub1_marks = float(data.get("sub1_marks"))
        sub2_marks = float(data.get("sub2_marks"))
        sub3_marks = float(data.get("sub3_marks"))
        sub4_marks = float(data.get("sub4_marks"))
        sub5_marks = float(data.get("sub5_marks"))
        percentage = (sub1_marks+sub2_marks+sub3_marks+sub4_marks+sub5_marks)/5
        percentage = float(f'{percentage:.2f}')
        student = Student.objects.filter(id=id).update(name=name,std_id=std_id,sub1_marks=sub1_marks,sub2_marks=sub2_marks,sub3_marks=sub3_marks,sub4_marks=sub4_marks, sub5_marks=sub5_marks, percentage=percentage)
        return redirect('/')
    return render(request, "index.html", context)