from django.db import models

# Create your models here.
class correos_enviados(models.Model):
    #PK
    id = models.BigAutoField(primary_key=True)

    #
    subject = models.CharField(max_length=100,blank=True,null=True)
    message = models.CharField(max_length=500,blank=True,null=True) 
    ip = models.CharField(max_length=100,blank=True,null=True)