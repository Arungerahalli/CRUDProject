from django.db import models

# Create your models here.
class CRUDApp_StudentTable(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=20)
    TestScore=models.FloatField()

#  'crudapp_crudapp_studenttable'
   
