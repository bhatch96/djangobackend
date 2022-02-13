from email.policy import default
from importlib.metadata import requires
from django.contrib.auth.models import User
from django.db import models

 
class Company(models.Model):
    cname = models.CharField(max_length=100)

    def __str__(self):
         return self.cname
    class Meta:
        db_table = "company" 

class Employee(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.User.first_name(null=False, default="user")
    # eid = models.CharField(max_length=20)  
    # ename = models.CharField(max_length=100)  
    # eemail = models.EmailField()  
    # econtact = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.user.first_name
    class Meta:  
        db_table = "employee"  
