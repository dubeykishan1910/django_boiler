from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number','first_name','last_name','email','fiels_of_study','cgpa'] #this is taken form models variable or fields='__all__'
        labels = {
              #html name           shown on html label
            'student_number' :  'Student Number',
            'first_name'     :  'First Name',
            'last_name'      :  'Last Name',
            'email'          :  'Email',
            'fiels_of_study' :  'Fiels of Study',
            'cgpa'           :  'CGPA_new'
        }

        # html form validation and css of bootstrap
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fiels_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'cgpa': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }