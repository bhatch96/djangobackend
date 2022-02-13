from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm, CompanyForm, UserUpdateForm, ChangeCompany
from employee.models import Employee, Company 
from django.views import View 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from employee.forms import SignUpForm
from django.contrib.auth.models import User
from django.views import generic
# class displaycompany(generic.ListView):
#     model = Company
#     template_name = 'booking/booktimes.html'
#     context_object_name = 'booktimes_list'

#     def get_queryset(self):
#         return BookTime.objects.filter(bookdate_id=self.kwargs['pk']).order_by('booktime')

#EMPLOYEE
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/show')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = User.objects.get(id=id)  
    form = ChangeCompany(instance=employee)

    if request.method == 'POST':
        form = ChangeCompany(request.POST, instance=employee)
        if form.is_valid:
            form.save()
            return redirect('/show')

    return render(request,'edit.html', {'form':form})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request, 'index copy.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

#COMPANY
def companyemp(request):  
    if request.method == "POST":  
        form = CompanyForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/company/show')  
            except: 
                pass  
    else:  
        form = CompanyForm()  
    return render(request,'companyindex.html',{'form':form})  
def companyshow(request):  
    companies = Company.objects.all()  
    return render(request,"companyshow.html",{'companies':companies})  
def companyedit(request, id):  
    company = Company.objects.get(id=id)  
    return render(request,'companyedit.html', {'company':company})  
def companyupdate(request, id):  
    company = Company.objects.get(id=id)  
    form = CompanyForm(request.POST, instance = company)  
    if form.is_valid():  
        form.save()  
        return redirect("/company/show")  
    return render(request, 'companyedit.html', {'company': company})  
def companydestroy(request, id):  
    company = Company.objects.get(id=id)  
    company.delete()  
    return redirect("/company/show")  

