from django.db import models

# Create your models here.

class DataModel(models.Model):
    title=models.CharField(max_length=400)
    email=models.EmailField(null=False,blank=False)
    message=models.TextField()

    def __str__(self):
        return self.email
