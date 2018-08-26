from django.db import models

# Create your models here.

class User(models.Model):
    UserID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Contact = models.IntegerField(default=0, blank=True, null=True)
    Address = models.TextField(max_length=100)
    
    def __str__(self):
        return str(self.UserID)
