from django.db import models
from django.utils.timezone import now

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	message=models.TextField()
	timestamp = models.DateTimeField(default=now())

# Create your models here.
