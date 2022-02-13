from xml.dom import ValidationErr
from django import forms  
# from employee.admin import Employee

from employee.models import Employee,Company  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# class CompanyFilter(django_filters.FilterSet):
#     class Meta:
#         model = Employee
#         fields = ['Company']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ChangeCompany (forms.ModelForm):
    id = id
    company = Company.cname
    
    class Meta:
        model = Employee
        fields = ('id','company')
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
class EmployeeForm(forms.ModelForm):
    first_name = User.first_name 
    email = User.email   
    class Meta: 
        model = Employee  
        fields = "__all__"  

# class EmployeeUpdateForm(forms.ModelForm):
#     first_name = User.first_name 
#     email = User.email   
#     company = Employee.company
#     class Meta: 
#         models = Employee, User
#         fields = "__all__"

from employee.models import Company  
class CompanyForm(forms.ModelForm):  
    class Meta:  
        model = Company  
        fields = "__all__"  