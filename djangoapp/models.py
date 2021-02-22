from django.db import models


# Create your models here.
class sample(models.Model):
    name=models.CharField(max_length=25)
    phone=models.IntegerField()
    def __str__(self):
        return self.name
class posts(models.Model):
    post_number=models.IntegerField()
    message=models.CharField(max_length=25)
    def __str__(self):
        return self.post_number        
class post(models.Model):
    name=models.CharField(max_length=25)
    post_number=models.IntegerField()
    message=models.CharField(max_length=25)
    def __str__(self):
        return self.name                
       