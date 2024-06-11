from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import random
from datetime import datetime


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True ,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    parent_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300 , null=True , blank=True)
    parent_phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        if not self.roll_number:
            latest_student = Student.objects.order_by('-roll_number').first()
            if latest_student:
                latest_roll_number = latest_student.roll_number
                last_number = int(latest_roll_number.split('-')[-1])
                new_number = last_number + 1
                self.roll_number = f"S-{str(datetime.now().year)}-{str(new_number).zfill(4)}"
            else:
                self.roll_number = f"S-{str(datetime.now().year)}-0001"
        super().save(*args, **kwargs)
        
        

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add attributes for driver
    contact_number = models.CharField(max_length=15, null=True , blank=True)
    title = models.CharField(max_length=300,null=True , blank=True)
    gender = models.CharField(max_length=100 , null=True , blank=True)
    address = models.CharField(max_length=255 ,null=True , blank=True)
    location = models.CharField(max_length=100, null=True , blank=True)
    driver_id = models.CharField(max_length=20, unique=True, editable=False)

    def __str__(self):
        return self.driver_id

    def save(self, *args, **kwargs):
        if not self.driver_id:
            # year = str(self.date_of_birth.year) if self.date_of_birth else str(datetime.now().year)
            year = str(datetime.now().year)
            last_driver_id = Driver.objects.order_by('-id').first()
            if last_driver_id:
                last_id = int(last_driver_id.driver_id.split('-')[-1])
                new_id = str(last_id + 1).zfill(4)
            else:
                new_id = '0001'
            self.driver_id = f'D-{year}-{new_id}'
        super().save(*args, **kwargs)

class Patron(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, null=True , blank=True)
    roll_number = models.CharField(max_length=20, unique=True ,null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    region = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.roll_number:
            latest_patron = Patron.objects.order_by('-roll_number').first()
            if latest_patron:
                latest_roll_number = latest_patron.roll_number
                last_number = int(latest_roll_number.split('-')[-1])
                new_number = last_number + 1
                self.roll_number = f"G-{str(datetime.now().year)}-{str(new_number).zfill(4)}"
            else:
                self.roll_number = f"G-{str(datetime.now().year)}-0001"
        super().save(*args, **kwargs) 


class Bus(models.Model):
    number = models.CharField(max_length=20, unique=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='driven_buses')


    def __str__(self):
        return self.number

    def clean(self):
        # Check if the driver is already assigned to another bus
        if self.driver and Bus.objects.exclude(id=self.id).filter(driver=self.driver).exists():
            raise ValidationError("This driver is already assigned to another bus.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class Route(models.Model):
    name = models.CharField(max_length=100)
    starting_point = models.CharField(max_length=255)
    ending_point = models.CharField(max_length=255)
    description = models.TextField()
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True, blank=True, related_name='routes')

    def __str__(self):
        return self.name
    
    
    