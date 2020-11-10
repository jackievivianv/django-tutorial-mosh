from django.db import models

# Create your models here. The model module allows us to create the necessary model to hold the data without us having to write the code.

class Product(models.Model):
	name = models.CharField(max_length=255) #set max length to prohibit overly long names
	price = models.FloatField() # for floating point numbers
	stock = models.IntegerField()
	image_irl = models.CharField(max_length=2083) #2083 standard max length for urls


