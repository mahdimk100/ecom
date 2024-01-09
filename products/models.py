from django.db import models
from base.models import BaseModel

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload='categories')
    
    def __str__(self):
        return self.category_name