from django.db import models
import uuid


# Create your models here.

class EditablePage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name_heading = models.CharField(max_length=50)
    name_content = models.CharField(max_length=100)

    occupation_heading = models.CharField(max_length=50)
    occupation_content = models.CharField(max_length=100)

    country_heading = models.CharField(max_length=50)
    country_content = models.CharField(max_length=100)

    image_img = models.ImageField(upload_to='images/', blank=True)

    txt_over_img = models.CharField(max_length=50)
