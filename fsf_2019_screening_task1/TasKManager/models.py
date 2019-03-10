from django.db import models
from django.utils import timezone

# Create your models here.

class Team(models.Model):
    Leader_name=models.CharFiels(max_length=120)
    Team_Name=models.TextField()
    permission=models.TextField()
    task=models.TextField()
    Team_id=models.IntegerField()
    created_date=models.DateTimeField(default = timezone.now)
    complete_date=models.DateTimeField(blank=True,null=True)

    def __str__ (self):
        return self.task +'-'+ self.Team_Name

class Users(models.Model):
    
    
