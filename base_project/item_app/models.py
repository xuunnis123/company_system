from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Item(models.Model):
    item_name=models.CharField(max_length=264)
    quantity=models.FloatField(null=True)
    unit=models.CharField(max_length=64)
    price=models.IntegerField(null=True)
    note=models.TextField(max_length=264)

    def __str__(self):
        return str(self.item_name)+str(":")+str(self.item_name)
    
    def get_absolute_url(self):
        return reverse("item_app:detail", kwargs={"pk": self.pk})

