from django.db import models

# Create your models here.
class EventQuery(models.Model):
   
    
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20,null=True,blank=True)
    event = models.CharField(max_length=20,null=True,blank=True)
    confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return f"{self.name}"
    
class Events(models.Model):
    video=models.FileField(upload_to="gallery",null=True,blank=True)
    title=models.CharField(max_length=50,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.title}"

class Banner(models.Model):
    image1=models.ImageField(upload_to="gallery",null=True,blank=True)
    image2=models.ImageField(upload_to="gallery",null=True,blank=True)
    image3=models.ImageField(upload_to="gallery",null=True,blank=True)
    image4=models.ImageField(upload_to="gallery",null=True,blank=True)