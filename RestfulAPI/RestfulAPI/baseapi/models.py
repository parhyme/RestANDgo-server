from django.db import models

class MobileInfo(models.Model):
    id = models.CharField(max_length=200, null=False, primary_key=True, default='default')
    android_id = models.CharField(max_length=200, null=True)
    model_name = models.CharField(max_length=200, null=True)
    battery_level = models.IntegerField(null=True)
    android_version = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	    return self.model_name

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
