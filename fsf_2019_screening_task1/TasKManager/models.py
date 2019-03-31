from django.db import models
from django.utils import timezone


# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=40)
    confrom_pass = models.CharField(max_length=40)

    def __str__(self):
        return self.username


class Task(models.Model):
    status_choice = (
        ('INPROGRESS', 'Inprogress'), ('NOT ASSIGNED', 'Not assigned'), ('DONE', 'done'), ('PLANNED', 'Planned'))
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=150)
    Description = models.TextField(blank=True)
    Assignee = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Status = models.CharField(choices=status_choice, default='NOT ASSIGNED', blank=False, max_length=50)
    Time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title, self.Assignee


class Team(models.Model):
    Creator_name = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='teams')
    Team_Name = models.CharField(max_length=100)
    members = models.ManyToManyField(SignUp)
    description = models.TextField(max_length=1024,blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    # logo = models.ImageField(blank=True)
    def __str__(self):
        return self.Team_Name
