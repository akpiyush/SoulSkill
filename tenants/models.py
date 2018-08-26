from django.db import models

# Create your models here.

class Tenants(models.Model):
    TenantID = models.AutoField(primary_key = True)
    TenantName = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.TenantName)

class User(models.Model):
    TenantID = models.ForeignKey('Tenants', blank=True, null=True, on_delete=models.CASCADE)
    UserID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Contact = models.IntegerField(default=0, blank=True, null=True)
    Address = models.TextField(max_length=100)
    
    def __str__(self):
        return str(self.UserID)
