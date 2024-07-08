from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length = 255,null = True)
    lastname = models.CharField(max_length= 255,null = True)
    phone = models.IntegerField(null= True)
    joined_date = models.DateField(null= True)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
    
    
from django.db import models

from mongoengine import Document, DynamicField

class DynamicDocument(Document):
    data = DynamicField()

    def __str__(self):
        return str(self.data)