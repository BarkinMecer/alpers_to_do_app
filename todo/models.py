from django.db import models
from django.utils import timezone

import datetime


class Branch(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name



class Todo(models.Model):

    activity_choices = [
        ('A', 'active'),
        ('P', 'passive')
    ]

    importance_d = [
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High')
    ]

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    activity = models.CharField(max_length=1, choices=activity_choices, default='A')
    importance = models.IntegerField(choices=importance_d, default=1)
    time_created = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateField(null=True)
    finish_time = models.TimeField(null=True)
    title = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def time_remain(self):
        return  datetime.datetime.combine(self.finish_date, self.finish_time) -  timezone.localtime(timezone.now()).replace(tzinfo=None) 
    
    def soon_come(self):
        return self.time_remain() < datetime.timedelta(days=3) 
    

    def time_up(self):
        return self.finish_date < timezone.now().date()

    
    class Meta:
        ordering = [ "finish_date", "finish_time","-importance"]



