from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayStudent ,name = 'display-student'),
    path('add-student/', views.addStudent, name = 'add-student'),
    path('update-student/<int:id>', views.updateStudent, name = 'update-student'),
    path('delete-student/<int:id>', views.deleteStudent, name = 'delete-student'),
   
]

