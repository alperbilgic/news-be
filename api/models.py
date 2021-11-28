from django.db import models
import uuid


# Create your models here.
class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=250)
    detail = models.CharField(max_length=4095)
    image = models.ImageField(null=True, blank=True, upload_to='news')
    date = models.DateTimeField(editable=True)