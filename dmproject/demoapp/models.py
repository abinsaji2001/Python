from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class person(models.Model):
    img2=models.ImageField(upload_to='pics')
    name2=models.CharField(max_length=250)
    desc2=models.TextField()
    def __str__(self):
        return self.name2
