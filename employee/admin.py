from django.contrib import admin

# # Register your models here.
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.base import Model
# from django.db.models.deletion import CASCADE
# from employee.models import Company
# # Create your models here.
# class Employee(models.Model):  
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # eid = models.CharField(max_length=20)  
#     ename = models.CharField(max_length=100)  
#     eemail = models.EmailField()  
#     econtact = models.CharField(max_length=15)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
#     def __str__(self):
#         return "__all__"