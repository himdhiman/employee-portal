from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from api import models
from django.contrib.auth.decorators import login_required


class Index(TemplateView):
    template_name = "api/index.html"


def adminLogin(request):
    if(request.method == "POST"):
        mailId = request.POST.get('mail')
        passWord = request.POST.get('password')
        
        user = authenticate(email = mailId, password=passWord, is_admin = True)

        if user is not None:
            login(request, user)
            return render(request, 'api/adminpanel.html')

        else:
            return render(request, 'api/adminlogin.html', {"error": "invalid credentials"})
    else:
        return render(request, 'api/adminlogin.html', {"error" : " "})

@login_required(login_url='/auth/admin/')
def createEmployee(request):
    genderMapping = {
        "Male" : "M",
        "Female" : "F",
        "Others" : "O"
    }
    if(request.method == "POST"):
        mailId = request.POST.get('mail')
        fName = request.POST.get('fname')
        lName = request.POST.get('lname')
        gender = genderMapping[request.POST.get('gender')]
        sal = request.POST.get('sal')
        passWord = request.POST.get('password')

        user = models.CustomUser(email = mailId, first_Name = fName, last_Name = lName, gender = gender, salary = sal)
        user.set_password(passWord)

        try:
            user.save()
            return render(request, 'api/createEmployee.html', {"success" : "Employee Created Successfully", "error" : ""})
        except:
            return render(request, 'api/createEmployee.html', {"error" : "mailId should be Unique", "success" : ""})
    else:
        return render(request, 'api/createEmployee.html', {"error" : "", "success" : ""})

@login_required(login_url='/auth/admin/')
def getEmployeeList(request):
    lst = models.CustomUser.objects.all();
    return render(request, 'api/employeelist.html', {"lst" : lst})


def employeeLogin(request):
    if(request.method == "POST"):
        mailId = request.POST.get('mail')
        passWord = request.POST.get('password')
        
        user = authenticate(email = mailId, password=passWord, is_admin = False)

        if user is not None:
            login(request, user)
            lst = models.CustomUser.objects.filter(email = mailId)
            print(lst)
            return render(request, 'api/employeepanel.html', {"lst" : lst})

        else:
            return render(request, 'api/employeelogin.html', {"error": "invalid credentials"})
    else:
        return render(request, 'api/employeelogin.html', {"error" : " "})

@login_required(login_url='/auth/admin/')
def editEmployee(request):
    obj = models.CustomUser.objects.all()
    if(request.method == "POST"):
        user = models.CustomUser.objects.get(email = request.POST.get("userdet"));
        user.salary = request.POST.get("sal")
        user.save()
        return render(request, 'api/editemployee.html', {"lst" : obj, "mess" : "Saved !"})
    else:
        return render(request, 'api/editemployee.html', {"lst" : obj, "mess" : ""})

def Logout(request):
    logout(request)
    return render(request, 'api/index.html')

