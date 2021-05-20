from django.urls import path
from django.urls import path
from api import views

urlpatterns = [
    path("", views.Index.as_view(), name = "index"),
    path("auth/admin/", views.adminLogin, name = 'adminlogin'),
    path("auth/employee/", views.employeeLogin, name = 'employeelogin'),
    path("auth/admin/createemployee", views.createEmployee, name = "createemployee"),
    path("auth/admin/getlist", views.getEmployeeList, name = "getlist"),
    path("auth/admin/editemployee", views.editEmployee, name = "editemployee")

]