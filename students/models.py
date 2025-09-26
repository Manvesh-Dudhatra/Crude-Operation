from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    std = models.IntegerField()

    class Meta:
        db_table = 'student'
    
