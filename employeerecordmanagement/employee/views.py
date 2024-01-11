from django.shortcuts import render,redirect

from django.contrib.auth import login,logout,authenticate  ## login is a inbuilt function to check the mathch so we are impoting it

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
             EmployeeDetail.objects.create(user=user,empcode=ec)
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
            login(request,user)
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