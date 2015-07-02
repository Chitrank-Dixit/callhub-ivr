from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime
# Create your models here.

class IvrData(models.Model):
	ivr_name = models.CharField(max_length=120)
	ivr_message = models.TextField(max_length=500)
	ivr_no_input_message = models.TextField(max_length=500)
	ivr_wrong_input_message = models.TextField(max_length=500)
	ip_zero = models.TextField(max_length=500, default='Invalid Input')
	ip_one = models.TextField(max_length=500 , default='Invalid Input')
	ip_two = models.TextField(max_length=500 , default='Invalid Input')
	ip_three = models.TextField(max_length=500 , default='Invalid Input')
	ip_four = models.TextField(max_length=500 , default='Invalid Input')
	ip_five = models.TextField(max_length=500 , default='Invalid Input')
	ip_six = models.TextField(max_length=500 , default='Invalid Input')
	ip_seven = models.TextField(max_length=500 , default='Invalid Input')
	ip_eight = models.TextField(max_length=500 , default='Invalid Input')
	ip_nine = models.TextField(max_length=500 , default='Invalid Input')
	timestamp = models.DateTimeField(auto_now_add = True)#, auto_now=False, default = now)
	updated = models.DateTimeField(auto_now_add = True)#, auto_now=False, default = now)
	user = models.ForeignKey(User)




