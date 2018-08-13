from django.db import models


class Post(models.Model):
	vehicleType = models.CharField(max_length=200,blank = True)
	number = models.CharField(max_length=10, blank = True)
	amount = models.CharField(max_length=3, blank = True)
	timeIn = models.CharField(max_length=30, blank = True)

	def __str__(self):
		return self.number