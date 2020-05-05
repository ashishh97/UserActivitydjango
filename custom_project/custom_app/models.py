from django.db import models

# Create your models here.

class User(models.Model):
  emp_id = models.CharField(max_length = 20)
  name = models.CharField(max_length=64)
  timezone = models.CharField(max_length=128)

  def __str__(self):
    return self.name

class ActivityPeriod(models.Model):
  starttime = models.DateTimeField()
  endtime = models.DateTimeField()
  user_id = models.ForeignKey(User, on_delete = models.CASCADE)

