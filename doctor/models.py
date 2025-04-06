from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True,verbose_name='نام و نام خانوادگی')
    specialist = models.CharField(max_length=200, null=True, blank=True,verbose_name='تخصص')
    education = models.CharField(max_length=200, null=True, blank=True,verbose_name='تحصیلات')
    image = models.ImageField(null=True, blank=True,verbose_name='عکس')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
