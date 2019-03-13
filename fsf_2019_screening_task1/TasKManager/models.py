from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    Team_Name=models.CharField(max_length=100)
    Name=models.CharField(max_length=120)
    Permission=models.CharField(max_length=50)
    Username=models.CharField(max_length=70)
    Password=models.CharField(max_length=50)
    ConfirmPassword=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)

    def __str__ (self):
        return self.Name

class Team(models.Model):
    Creator_name=models.CharField(max_length=120)
    Team_Name=models.CharField(max_length=100)
    members=models.ManyToManyField(Users)
    created_date=models.DateTimeField(default = timezone.now)
    
    def __str__ (self):
        return self.Team_Name



class Task(models.Model):
    status_choice=(('PLANNING','Planning'),('PLANNED','Planned'),
                   ('INPROGRESS','Inprogress'),('DONE','Done'))
    Title=models.CharField(max_length=200)
    Team=models.ForeignKey(Team,on_delete=models.CASCADE)
    Descripton=models.TextField()
    Assignee=models.ForeignKey(Users,on_delete=models.CASCADE)
    Status=models.CharField(max_length=10,choices=status_choice,default='PLANNING')

    def __str__ (self):
        return self.Title +'-'+self.Assignee

class TeamCreater(models.Model):
    Users=models.ForeignKey(Users,on_delete=models.CASCADE)

    def __str__(self):
        return self.Users.Name

    
    
