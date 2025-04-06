
from django.db import models
from doctor.models import Doctor
from django.utils import timezone


class AppointmentDay(models.Model):
    date = models.DateField(verbose_name='روز',blank=True,null=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f"{self.date}"


class Appointment(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام و نام خانوادگی بیمار')
    phone = models.CharField(max_length=11,verbose_name='شماره تلفن')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=True,verbose_name='دکتر')
    day = models.ForeignKey(AppointmentDay, on_delete=models.CASCADE, related_name='day',verbose_name='روز',blank=True,null=True)
    time = models.TimeField(verbose_name='ساعت')

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return f"{self.name}"
