from django.db import models
from django.utils.timezone import now

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	message=models.TextField()
	timestamp = models.DateTimeField(default=now())

	def __str__(self):
		return self.name + ', ' + self.email + ', submitted on ' + self.timestamp.strftime("%Y-%m-%d %H:%M")

# Create your models here.
