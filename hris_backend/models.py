from django.db import models

# Create your models here.


class Employeeleave(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Reason = models.CharField(max_length=100)
    leave_date = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name
