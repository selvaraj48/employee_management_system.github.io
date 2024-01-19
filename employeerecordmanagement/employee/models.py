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

class EmployeeEducation(models.Model):
    
        user = models.ForeignKey(User ,on_delete=models.CASCADE) #we will store all the information about the userrs like first name last name and emailid in the user model..
        coursepg =models.CharField(max_length=150,null=True) #null = true means its not important if u leave the table blank also it wont care
        schoolclgpg =models.CharField(max_length=300,null=True)
        yearofpassingpg =models.CharField(max_length=100,null=True)
        percentagepg =models.CharField(max_length=50,null=True)
        coursegra =models.CharField(max_length=150,null=True) #null = true means its not important if u leave the table blank also it wont care
        schoolclggra =models.CharField(max_length=300,null=True)
        yearofpassinggra =models.CharField(max_length=100,null=True)
        percentagegra =models.CharField(max_length=50,null=True)
        coursessc =models.CharField(max_length=150,null=True) #null = true means its not important if u leave the table blank also it wont care
        schoolclgssc =models.CharField(max_length=300,null=True)
        yearofpassingssc =models.CharField(max_length=100,null=True)
        percentagessc =models.CharField(max_length=50,null=True)
        coursehsc =models.CharField(max_length=150,null=True) #null = true means its not important if u leave the table blank also it wont care
        schoolclghsc =models.CharField(max_length=300,null=True)
        yearofpassinghsc =models.CharField(max_length=100,null=True)
        percentagehsc =models.CharField(max_length=50,null=True)
        
        def __str__(self):
                return self.user.username
        

class EmployeeExperience(models.Model):
    
        user = models.ForeignKey(User ,on_delete=models.CASCADE) #we will store all the information about the userrs like first name last name and emailid in the user model..
        company1name =models.CharField(max_length=150,null=True) #null = true means its not important if u leave the table blank also it wont care
        company1desig =models.CharField(max_length=300,null=True)
        company1salary =models.CharField(max_length=100,null=True)
        company1duration =models.CharField(max_length=50,null=True)
        company2name =models.CharField(max_length=150,null=True) #null = true means its not important if u leave the table blank also it wont care
        company2desig =models.CharField(max_length=300,null=True)
        company2salary =models.CharField(max_length=100,null=True)
        company2duration =models.CharField(max_length=50,null=True)
        company3name =models.CharField(max_length=150,null=True) #null = true means its not important if u leave the table blank also it wont care
        company3desig =models.CharField(max_length=300,null=True)
        company3salary =models.CharField(max_length=100,null=True)
        company3duration =models.CharField(max_length=50,null=True)

        
        def __str__(self):
                return self.user.username