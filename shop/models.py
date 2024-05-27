from django.db import models
import datetime
import os

# Create your models here.
def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename= f"{filename}_{now_time}"
    
    return os.path.join('upload/', new_filename)

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-hidden, 1-show")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-hidden, 1-show")
    trending = models.BooleanField(default=False, help_text="0-default, 1-trending")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
