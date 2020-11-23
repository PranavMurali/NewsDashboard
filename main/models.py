from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#databse table stuff
class Marks(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    date_modified=models.DateTimeField(auto_now=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    score= models.IntegerField(default=0)
    
    def __str__(self):
        return self.title