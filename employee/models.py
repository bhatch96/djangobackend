from django.db import models
 
class Company(models.Model):
    cname = models.CharField(max_length=100)

    class Meta:
        db_table = "company" 

class Employee(models.Model):  
    # eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, default=1)

    class Meta:  
        db_table = "employee"  
