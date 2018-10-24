from django.db import models

# Create your models here.

class Lore(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(upload_to='media', null='False')
	
	
	def __str__(self):
		return self.title