from django.db import models

# Create your models here.
class Contact(models.Model):
    emailid=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    query=models.CharField(max_length=150)
    name=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name