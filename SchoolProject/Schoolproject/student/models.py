from django.db import models
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length=40)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Person(models.Model):
    GENDER_CHOICES=(('male','Male'),('female','female'),)
    PURPOSE=(('enquiry','For Enquiry'),('order','Place Order'),('return','Return'),)
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=8)
    age=models.CharField(max_length=2)
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES,)
    phone_number=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    purpose = models.CharField(max_length=10, choices=PURPOSE, )
    pen=models.BooleanField("pen")

    def __str__(self):
        return self.name