from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from utility.constants.department import DEPARTMENT_TYPE


class Employee(models.Model):
    user = models.OneToOneField(User, related_name="Employee", blank=True, null=True, on_delete=models.CASCADE)
    company_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    national_id = models.CharField(max_length=11, blank=True, null=True)
    marital_status = models.CharField(max_length=255, blank=True, null=True)
    name_spouse = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    personal_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    date_joining = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=32,
                              choices=(('active', 'active'), ('inactive', 'inactive')),
                              blank=True
                              )
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    department = models.CharField(max_length=35, choices=DEPARTMENT_TYPE, blank=True, null=True)
    picture = models.ImageField(upload_to='hr/documents/%Y/%m/%d', blank=True, null=True)

    class Meta:
        ordering = ['company_id']

    def __str__(self):
        return f'{self.company_id} - {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.email:  # Only generate email if it's not provided
            # pakeisti lietuviškas raides.
            translation_table = str.maketrans("ąčęėįšųū ", "aceeisuu_")
            self.email = f"{self.first_name.lower().translate(translation_table)}.{self.last_name.lower().translate(translation_table)}@pvz.lt"
        super().save(*args, **kwargs)
