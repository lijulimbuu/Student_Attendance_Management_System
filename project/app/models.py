from django.db import models

# Create your models here.
class Register_User(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    year = models.IntegerField()
    
    def __str__(self):
        return self.name