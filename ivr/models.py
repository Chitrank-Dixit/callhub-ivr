from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime
# Create your models here.

class IvrData(models.Model):
	ivr_message = models.CharField(max_length=500)
	ivr_no_input_message = models.TextField(max_length=500)
	ivr_wrong_input_message = models.TextField(max_length=500)
	ip_zero = models.CharField(max_length=500)
	ip_one = models.CharField(max_length=500)
	ip_two = models.CharField(max_length=500)
	ip_three = models.CharField(max_length=500)
	ip_four = models.CharField(max_length=500)
	ip_five = models.CharField(max_length=500)
	ip_six = models.CharField(max_length=500)
	ip_seven = models.CharField(max_length=500)
	ip_eight = models.CharField(max_length=500)
	ip_nine = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add = True)#, auto_now=False, default = now)
	updated = models.DateTimeField(auto_now_add = True)#, auto_now=False, default = now)
	user = models.ForeignKey(User)




