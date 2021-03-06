from django.db import models


class Post(models.Model):
    vehicleType = models.CharField(max_length=200, blank=True)
    number = models.CharField(max_length=10, blank=True, primary_key=True)
    amount = models.CharField(max_length=3, blank=True)
    timeIn = models.CharField(max_length=30, blank=True)
    timeOut = models.CharField(max_length=30, blank=True)
    date = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.number

    def setTimeOut(self, timeOut):
        return self.timeOut


class DatePost(models.Model):
    #vehicleNumber = models.CharField(max_length=10, blank=True, primary_key=True,default='number')
    #date = models.CharField(max_length=50, blank=True)
    vehicleNumber=models.ForeignKey(Post, on_delete=models.CASCADE, max_length=10)
    date=models.CharField(max_length=25, blank=True)
    id=models.IntegerField(primary_key=True)