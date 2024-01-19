from django.shortcuts import render,redirect

from django.contrib.auth import login as auth_login,logout,authenticate  ## login is a inbuilt function to check the mathch so we are impoting it

from .models import * # since we need to use or update the model we have alredy creted ... we need to import it

# Create your views here.
def index(request):         #in urls prgm we have a function which will redirect here .. so here we do the function request
    return render(request,'index.html') 


def registration(request):
#now we are going to get info from the form (its more are like retriving information from the post method)
    error=""
    if request.method == "POST":
        fn=request.POST.get('firstname')   
        ln=request.POST.get('lastname')
        ec=request.POST.get('empcode')
        em=request.POST.get('email')
        pwd=request.POST.get('password') 

        #now we need to update the got information to our database
        
        try:
             user= User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)  ## in our database the user name is email id bcz we have assaigned here like that
             EmployeeDetail.objects.create(user=user,empcode=ec) # here we are storing foreignkey usr in employeedetails to access that specific employee details
             EmployeeExperience.objects.create(user=user)
             EmployeeEducation.objects.create(user=user)
             error="no" # just to display that there is no error we created the variable error

        except:
            error="yes"

    return render(request,'registration.html',locals()) # here we are rendering the local as well bcz we nee to return the local variable value error to the registration page

#now we are going to redirect the user to login page after the registration page or we can redirect to home page as well

def emp_login(request):
    error=""
    if request.method == 'POST':
        login_un = request.POST.get('emailid')
        login_pwd = request.POST.get('password')

        user=authenticate(username=login_un,password=login_pwd)  # authenticate is a inbuilt function which chenck with the database whether there is a data similar to the entered valuess..
        
        if user: # here we are checking that ... if the above user values all are crct then ther user store report accordingly value noqw we are checking its storing tr or false
            auth_login(request,user)  # here i got a problem while importing login model as login like u cant have 2 values so i  imported login as auth_login  this error occurs bcz having same name to diff module
            error="no"
        else:
            error="yes"
    return render(request,'emp_login.html',locals())

def emp_home(request): #here we can simply see the sample employee home page but we need to acces that only with the loged in person so we apply a condition
    if not request.user.is_authenticated: #this the condition like whter the site is loged in or user loged in page or not
        return redirect('index')
    return render(request,"emp_home.html")

def profile(request):
#now we are going to get info from the form (its more are like retriving information from the post method)
    if not request.user.is_authenticated: #this the condition like whter the site is loged in or user loged in page or not
        return redirect('index')
    error=""
    user=request.user #by this we are getting the current user of the session and we are storing it in the user variable..
    employee=EmployeeDetail.objects.get(user=user) #in this case the above requested user details from the employee details is mathed and fetched
    if request.method == "POST":
        fn=request.POST.get('firstname')   
        ln=request.POST.get('lastname')
        ec=request.POST.get('empcode')
        dept=request.POST.get('department')
        desig=request.POST.get('designation') 
        cont=request.POST.get('contact')
        jd=request.POST.get('jdate')
        gd=request.POST.get('gender')

        #now we need to update the data since the data is already got during registration we are going to update it
        employee.user.first_name=fn
        employee.user.last_name=ln
        employee.empcode=ec
        employee.designation=desig
        employee.contact=cont
        employee.gender=gd
        employee.empdept=dept


        if jd: #here we are checking whether the jd variable has data (this condition os true or not)   // we cat fill joining date so we used this condition
         employee.joiningdate=jd
        try:
             employee.user.save()
             employee.save()
             error="no" # just to display that there is no error we created the variable error

        except:
            error="yes"

    return render(request,'profile.html',locals()) # here we are rendering the local as well bcz we nee to return the local variable value error to the registration page

#now we are going to redirect the user to login page after the registration page or we can redirect to home page as well

def Logout(request):
    logout(request) #logout is a predefined function so we are calling it
    return redirect('index') # as we assumed name to each page we used to call it with name

#now for admin login function

def admin_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user=authenticate(username=u,password=p)  # authenticate is a inbuilt function which chenck with the database whether there is a data similar to the entered valuess..
        try:
            if user.is_staff: # here we are checking that ... if the above user values all are crct then ther user store report accordingly value noqw we are checking its storing tr or false
                auth_login(request,user)  # here i got a problem while importing login model as login like u cant have 2 values so i  imported login as auth_login  this error occurs bcz having same name to diff module
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    return render(request,'admin_login.html',locals())


def myexperience(request):
    if not request.user.is_authenticated: #this the condition like whter the site is loged in or user loged in page or not
        return redirect('index')
    error = ""
    user=request.user #by this we are getting the current user of the session and we are storing it in the user variable..
    experience=EmployeeExperience.objects.get(user=user) #in this case the above requested user details from the employee experience model is matched and fetched

    return render(request,'myexperience.html',locals())


def edit_experience(request):
#now we are going to get info from the form (its more are like retriving information from the post method)
    if not request.user.is_authenticated: #this the condition like whter the site is loged in or user loged in page or not
        return redirect('index')
    error=""
    user=request.user #by this we are getting the current user of the session and we are storing it in the user variable..
    experience=EmployeeExperience.objects.get(user=user) #in this case the above requested user details from the employee details is mathed and fetched
    if request.method == "POST":
        c1n=request.POST.get('company1name')   
        c1d=request.POST.get('company1desig')
        c1s=request.POST.get('company1salary')
        c1du=request.POST.get('company1duration')
        c2n=request.POST.get('company1name')   
        c2d=request.POST.get('company1desig')
        c2s=request.POST.get('company1salary')
        c2du=request.POST.get('company1duration')
        c3n=request.POST.get('company1name')   
        c3d=request.POST.get('company1desig')
        c3s=request.POST.get('company1salary')
        c3du=request.POST.get('company1duration')
        

        #now we need to update the data since the data is already got during registration we are going to update it
        experience.company1name=c1n
        experience.company1desig=c1d
        experience.company1salary=c1s
        experience.company1duration=c1du
        experience.company2name=c2n
        experience.company2desig=c2d
        experience.company2salary=c2s
        experience.company2duration=c2du
        experience.company3name=c3n
        experience.company3desig=c3d
        experience.company3salary=c3s
        experience.company3duration=c3du

        try:
             experience.save()
             error="no" # just to display that there is no error we created the variable error

        except:
            error="yes"

    return render(request,'edit_experience.html',locals()) 

def myeducation(request):
    if not request.user.is_authenticated: #this the condition like whter the site is loged in or user loged in page or not
        return redirect('index')
    error = ""
    user=request.user #by this we are getting the current user of the session and we are storing it in the user variable..
    education=EmployeeEducation.objects.get(user=user) #in this case the above requested user details from the employee experience model is matched and fetched

    return render(request,'myeducation.html',locals())


def edit_myeducation(request):
#now we are going to get info from the form (its more are like retriving information from the post method)
    if not request.user.is_authenticated: #this the condition like whter the site is loged in or user loged in page or not
        return redirect('index')
    error=""
    user=request.user #by this we are getting the current user of the session and we are storing it in the user variable..
    education=EmployeeEducation.objects.get(user=user) #in this case the above requested user details from the employee details is mathed and fetched
    if request.method == "POST":
        cp=request.POST.get('coursepg')   
        sp=request.POST.get('schoolclgpg')
        yp=request.POST.get('yearofpassingpg')
        pp=request.POST.get('percentagepg')
        cg=request.POST.get('coursegra')   
        sg=request.POST.get('schoolclggra')
        yg=request.POST.get('yearofpassinggra')
        pg=request.POST.get('percentagegra')
        cs=request.POST.get('coursessc')   
        ss=request.POST.get('schoolclgssc')
        ys=request.POST.get('yearofpassingssc')
        ps=request.POST.get('percentagessc')
        ch=request.POST.get('coursehsc')   
        sh=request.POST.get('schoolclhsc')
        yh=request.POST.get('yearofpassinghsc')
        ph=request.POST.get('percentagehsc')
        
        

        #now we need to update the data since the data is already got during registration we are going to update it
        education.coursepg=cp
        education.schoolclgpg=sp
        education.yearofpassingpg=yp
        education.percentagepg=pp
        education.coursegra=cg
        education.schoolclggra=sg
        education.yearofpassinggra=yg
        education.percentagegra=pg
        education.coursessc=cs
        education.schoolclgssc=ss
        education.yearofpassingssc=ys
        education.percentagessc=ps
        education.coursehsc=ch
        education.schoolclghsc=sh
        education.yearofpassinghsc=yh
        education.percentagehsc=ph
        

        try:
             education.save()
             error="no" # just to display that there is no error we created the variable error

        except:
            error="yes"

    return render(request,'edit_myeducation.html',locals()) 

def change_password(request):
    if not request.user.is_authenticated: #this the condition like whter the site is loged in or user loged in page or not
        return redirect('emp_login')
    error = ""

    user=request.user #by this we are getting the current user of the session and we are storing it in the user variable..

    if request.method == "POST":
        c=request.POST.get('currentpassword')
        n=request.POST.get('newpassword')

        try:
            if user.check_password(c): #here check_password is a predefined function used to check the password
                user.set_password(n)
                user.save()
                error="no"
            else: 
                error="not"

        except:
            error="yes"

    return render(request,'change_password.html',locals())



def admin_home(request):
    user=request.user
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    return render(request,'admin_home.html',locals())


def change_adminpassword(request):
    if not request.user.is_authenticated: #this the condition like whter the site is loged in or user loged in page or not
        return redirect('admin_login')
    error = ""

    user=request.user #by this we are getting the current user of the session and we are storing it in the user variable..

    if request.method == "POST":
        c=request.POST.get('currentpassword')
        n=request.POST.get('newpassword')

        try:
            if user.check_password(c): #here check_password is a predefined function used to check the password
                user.set_password(n)
                user.save()
                error="no"
            else: 
                error="not"

        except:
            error="yes"

    return render(request,'change_adminpassword.html',locals())


def all_employees(request):
    user=request.user
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    employee=EmployeeDetail.objects.all()
    
    return render(request,'all_employees.html',locals())