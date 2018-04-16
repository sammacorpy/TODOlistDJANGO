from django.db import models
from datetime import datetime 
# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=40)
    desc=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    suspended=models.BooleanField(default=False)
    lastdate=models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title