# from djagno.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

from cities_light.models import Country, City, Region

# Create your models here.

# class State(models.Model):
#     state = models.ForeignKey(Region, on_delete=models.CASCADE)
#
#     def __str__():
#         return self.state
#
# class City1(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#
#     def __str__():
#         return self.city

class EmployeeProfileInfo(models.Model):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE,'Female'),
        (OTHER, 'Other'),
    )

    UNEDUCATED = "UE"
    FIFTH_TO_EIGHT = "F_E"
    NINTH_TO_TENTH = "N_T"
    ELEV_TO_TWELVE = "E_T"
    ITI = "ITI"
    UNDERGRAD = "UG"
    POSTGRAD = "PG"
    POLYTECH = "PT"
    DIPLOMA = "DP"
    BENGG = "BE"
    MENGG = "ME"
    BSC = "BSC"
    MSC = "MSC"
    BBA = "BBA"
    MBA = "MBA"
    MASTERSDEGREE = "MAD"
    BTECH = "BT"
    MTECH = "MT"
    BACHELORDEGREE = "BAD"
    educaton_choice = (
        (UNEDUCATED, 'Uneducated'),
        (FIFTH_TO_EIGHT, '5th to 8th'),
        (NINTH_TO_TENTH, '9th to 10th'),
        (ELEV_TO_TWELVE, '11th to 12th'),
        (ITI, 'ITI'),
        (UNDERGRAD, 'Under Graduate'),
        (POSTGRAD, 'Post Graduate'),
        (POLYTECH, 'Polytechnic'),
        (DIPLOMA, 'Diploma'),
        (BENGG, 'B.E'),
        (MENGG, 'M.E'),
        (BSC, 'B.Sc'),
        (MSC, 'M.Sc'),
        (BBA, 'BBA'),
        (MBA, 'MBA'),
        (BTECH, 'B.Tech'),
        (MTECH, 'M.Tech'),
        (MASTERSDEGREE, 'Master\'s Degree'),
        (BACHELORDEGREE, 'Bachelor\'s Degree'),
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    # additional
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=15)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    education = models.CharField(max_length=20, choices=educaton_choice)
    skillset = models.CharField(max_length=255)
    experince = models.CharField(max_length=2, blank = True)
    identification = models.CharField(max_length=50)

    resume = models.FileField(upload_to='resume', blank=True)

    def __str__(self):
        return self.user.email

class EmployerProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)

    # additional
    company_name = models.CharField(max_length=255)
    company_gst_no = models.CharField(max_length=50)
    company_cin = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=15)
    # required_skill = models.CharField(max_length=255)

    class Meta:
        unique_together = ('company_gst_no', 'company_cin', 'location',)

    def __str__(self):
        return self.user.username + ' ' + self.company_name
