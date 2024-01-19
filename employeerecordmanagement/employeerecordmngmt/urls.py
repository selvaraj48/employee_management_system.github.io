"""
URL configuration for employeerecordmngmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import *  ## to call the index function(below in the url pattern ) we need to import it so imported it..

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),       # inside this quotes ''   we assaign the url name like admin etc then after comma we call the function to render the page
    path('registration/',registration,name='registration'), # we are assaigning the name so that we can call the url name inside the html codes
    path('emp_login/',emp_login,name="emp_login"),
    path('emp_home/',emp_home,name="emp_home"),
    path('profile/',profile,name='profile'),
    path('logout/',Logout, name="logout"),
    path('admin_login',admin_login,name="admin_login"),
    path('myexperience/',myexperience,name="myexperience"),
    path('edit_experience/',edit_experience,name='edit_experience'),
    path('myeducation/',myeducation,name="myeducation"),
    path('edit_myeducation/',edit_myeducation,name="edit_myeducation"),
    path('change_password/',change_password,name="change_password"),
    path('admin_home/',admin_home,name="admin_home"),
    path('change_adminpassword/',change_adminpassword,name="change_adminpassword"),
    path('all_employees/',all_employees,name="all_employees")

]

