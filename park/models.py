from django.db import models

class Post(models.Model):
	vehicleType=models.CharField(max_length=200)
	number=models.CharField(max_length=10)
	amount=models.CharField(max_length=3)
	timeIn=models.CharField(max_length=30)
	def __str__(self):
		return self.number
		
