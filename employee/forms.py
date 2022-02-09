from django import forms  

from employee.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

from employee.models import Company  
class CompanyForm(forms.ModelForm):  
    class Meta:  
        model = Company  
        fields = "__all__"  