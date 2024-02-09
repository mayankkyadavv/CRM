from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#User = get_user_model() #imported from django.contrib.auth, default user model (not reccomended)
#feb 8th update: reviewed line of code, not reccomended because  it can cause issues with migrations and admin site if you change the user model in the future


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # similar to foreign key, must be linked to model (this case user) 
    # and have on_delete

    def __str__(self):
        return self.user.email   


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default = 0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    #ForeignKey must have on_delete
    #some options include:
    #models.CASCADE -> when agent is deleted delete lead aswell
    #models.SET_NULL -> sets to null, must have "null=True" aswell
    #models.SET_DEFAULT -> set to default, must have "default=" in code

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

