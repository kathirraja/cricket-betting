from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    name = models.CharField(blank=True,null=True,max_length=30)
    credits = models.IntegerField(blank=True,null=True,default=30)
    team = models.ForeignKey(
                    'bedding_admin.Team',
                    on_delete=models.CASCADE,
                    related_name='players',
                    null=True,
                )

class Person(models.Model):
    credits = models.IntegerField(default=500)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="person")