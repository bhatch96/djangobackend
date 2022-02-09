from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm, CompanyForm
from employee.models import Employee, Company  
# Create your views here.  
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
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

#EMPLOYEE
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
    return render(request,'companyindex.html',{'cform':form})  
def companyshow(request):  
    companies = Company.objects.all()  
    return render(request,"companyshow.html",{'company':companies})  
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
    return redirect("/companyshow")  

