from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='note/img/', null=True, blank=True)

    def __str__(self):
        return self.title
    
