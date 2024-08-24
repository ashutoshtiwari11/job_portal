# from django.contrib.auth.models import AbstractUser
# from django.db import models

# from account.managers import CustomUserManager

# JOB_TYPE = (
#     ('M', "Male"),
#     ('F', "Female"),

# )

# ROLE = (
#     ('employer', "Employer"),
#     ('employee', "Employee"),
# )

# class User(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True, blank=False,
#                               error_messages={
#                                   'unique': "A user with that email already exists.",
#                               })
#     role = models.CharField(choices=ROLE,  max_length=10)
#     gender = models.CharField(choices=JOB_TYPE, max_length=1)
#     aadhar = models.CharField(max_length=12)


#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return self.first_name+ ' ' + self.last_name
#     objects = CustomUserManager()

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False)
    role = models.CharField(max_length=10, choices=(('employer', 'Employer'), ('employee', 'Employee')))
    gender = models.CharField(max_length=1, choices=(('M', "Male"), ('F', "Female")))
    aadhar = models.CharField(max_length=12)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    img = models.ImageField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=255)
    pan = models.CharField(max_length=10, unique=True, blank='')
    gstin = models.CharField(max_length=15, unique=True, blank='')
    company_address = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.company_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    experience = models.JSONField()
    resume = models.FileField()
    skills= models.JSONField()
    portfolio = models.URLField()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.job_title}"

