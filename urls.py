from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views # type: ignore

urlpatterns = [
    path('',views.home,name='home'),
    path('employee_list',views.employee_list,name='employee_list'),
    path('employees/update/<int:employee_id>/', views.employee_update, name='employee_update'),
    path('employees/delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),
]
