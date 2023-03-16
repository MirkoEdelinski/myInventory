from django.db import models

class Items(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=50)
    item_stock = models.IntegerField(default=0)
    item_image = models.ImageField(null=True, blank=True, upload_to="images/")
