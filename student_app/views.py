from django.http import HttpResponseRedirect 
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    details = Student.objects.all()
    context={
        'students' : details,
    }
    return render(request, 'students/home.html', context)



def view_student(request, id):
    student = Student.objects.get(pk = id)
    return HttpResponseRedirect(reverse('index')) 



# geting data and validating it in forms
def add(request):
    if request.method == 'POST':
        
        form = StudentForm(request.POST)#puting all your form taken values in 
        
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['fiels_of_study']
            new_cgpa = form.cleaned_data['cgpa']

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                fiels_of_study = new_field_of_study,
                cgpa = new_cgpa
            )
            
            new_student.save()
            return render(request, 'students/add.html',{
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html',{
            'form': StudentForm()})




def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk = id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {'form':form,'success':True})
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        
    return render(request, 'students/edit.html', {'form':form})


def delete(request, pk):
    task = get_object_or_404(Student, pk=pk)
    task .delete()
    return redirect('index')