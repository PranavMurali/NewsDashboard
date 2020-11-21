from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#databse table stuff
class marks(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    date_modified=models.DateTimeField(auto_now=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title