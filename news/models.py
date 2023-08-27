from django.db import models

# Create your models here.
class news(models.Model):
   title=models.CharField(max_length=40) 
   txt=models.TextField(max_length=100)
   editor=models.CharField(max_length=15)
   dtm=models.CharField(max_length=10,default=1402/2/7)
   def __str__(self) -> str:
     return self.title
    
class contact(models.Model):
   name=models.CharField(max_length=30)  
   email=models.CharField(max_length=50)
   onvan=models.CharField(max_length=150)
   matn=models.CharField(max_length=500)