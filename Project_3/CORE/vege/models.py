from django.db import models

# Create your models here.
class Reciepe(models.Model):
    reciepe_name = models.CharField(max_length = 100)
    reciepe_descriptin = models.TextField()
    reciepe_image = models.ImageField(upload_to= "reciepe")

    