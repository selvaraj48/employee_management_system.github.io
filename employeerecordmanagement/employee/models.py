from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#now we are going to create database for the site 

class EmployeeDetail(models.Model):
    
        user = models.ForeignKey(User ,on_delete=models.CASCADE) #we will store all the information about the userrs like first name last name and emailid in the user model..
        empcode =models.CharField(max_length=50) #null = true means its not important if u leave the table blank also it wont care
        empdept =models.CharField(max_length=100,null=True)
        designation =models.CharField(max_length=100,null=True)
        contact =models.CharField(max_length=15,null=True)
        gender =models.CharField(max_length=50,null=True)
        joiningdate =models.DateField(null=True)  #for date we use date field and wee dont need to assaign the size for it
        def __str__(self):
                return self.user.username
        #these are the information we get from the user while updating profile to store that we created a data base
