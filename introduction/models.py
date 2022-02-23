from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    subject = models.TextField(max_length=100)



    def __str__(self):
        return self.name