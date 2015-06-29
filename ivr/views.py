import os
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
# Django Authentication builtins
from django.contrib import auth
from django.contrib.auth import login , logout
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponse , HttpRequest
# our django forms
from forms import UserForm , SignedUserForm, ConfigIvrForm


# flash messages in Django
from django.contrib import messages

# importing models
from models import IvrData

from django.template import RequestContext
# sending mail usin Django
from django.core.mail import send_mail
import plivoxml
from utils import joke_from_reddit


def home(request):
	title = "Welcome"
	context = {
		"template_title": title,
	}
			
	return render(request ,"index.html",context)

def login(request):
	title = "Login"
	context = {
		"template_title": title,
	}
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request,user)
			messages.success(request, request.POST.get('username')+' logged in')
			return HttpResponseRedirect('/')
		elif user is None:
			messages.error(request, 'Incorrect Username or Password')
			return HttpResponseRedirect('/login' ,messages)
	return render(request ,"login.html",context)


def register(request):
	title = "Register"
	send_email=''
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			new_user.save()
			new_user.backend='django.contrib.auth.backends.ModelBackend'
			auth.login(request,new_user)
			messages.success(request, 'Account with username '+request.POST.get('username')+' has been created')
			return HttpResponseRedirect('/')
		else:
			form = UserForm()
			messages.error(request, 'User already created please choose different username and email')
			return HttpResponseRedirect('/register' ,messages)

	context = {
	    "template_title": title,
	}
	return render(request ,"register.html",context)

def signout(request):
    logout(request)
    context = {}
    return render(request, "index.html",context)



def config_ivr(request):
	context = {
		"template_title": "Configure IVR"
	}
	print 'hii'
	if request.method == 'POST':
		form = ConfigIvrForm(request.POST)
		configure_ivr = IvrData()
		configure_ivr.ivr_name = request.POST['ivr_name']
		configure_ivr.ivr_message = request.POST['welcome_message']
		configure_ivr.ivr_no_input_message = request.POST['no_input_message']
		configure_ivr.ivr_wrong_input_message = request.POST['wrong_input_message']
		configure_ivr.ip_zero = request.POST['zeroip_message']  if (request.POST['zeroip_message']!='') else 'Invalid Input'
		configure_ivr.ip_one = request.POST['oneip_message']  if (request.POST['oneip_message']!='') else 'Invalid Input'
		configure_ivr.ip_two = request.POST['twoip_message']  if (request.POST['twoip_message']!='') else 'Invalid Input'
		configure_ivr.ip_three = request.POST['threeip_message']  if (request.POST['threeip_message']!='') else 'Invalid Input'
		configure_ivr.ip_four = request.POST['fourip_message']  if (request.POST['fourip_message']!='') else 'Invalid Input'
		configure_ivr.ip_five = request.POST['fiveip_message']  if (request.POST['fiveip_message']!='') else 'Invalid Input'
		configure_ivr.ip_six = request.POST['sixip_message']  if (request.POST['sixip_message']!='') else 'Invalid Input'
		configure_ivr.ip_seven = request.POST['sevenip_message']  if (request.POST['sevenip_message']!='') else 'Invalid Input'
		configure_ivr.ip_eight = request.POST['eightip_message']  if (request.POST['eightip_message']!='') else 'Invalid Input'
		configure_ivr.ip_nine = request.POST['nineip_message']  if (request.POST['nineip_message']!='') else 'Invalid Input'

		configure_ivr.user = request.user

		configure_ivr.save()
		print request.user

		return HttpResponseRedirect('/response/ivr/list/')
	return render(request,"config_ivr.html", context)

def ivrs(request):
	print request.user.id
	Ivrdata = IvrData.objects.all().filter(user_id=request.user.id)
	context = {
		"ivrdata": Ivrdata
	}	
	return render(request, "list_ivrs.html", context)


def ivr_edit(request, ivr_id, user_id):
	Ivrdata = IvrData.objects.get(id=ivr_id)
	context = {
		"template_title": "Ivr Edit",
		"ivr_name": Ivrdata.ivr_name,
		"ivr_message": Ivrdata.ivr_message,
		"ivr_no_input_message": Ivrdata.ivr_no_input_message,
		"ivr_wrong_input_message": Ivrdata.ivr_wrong_input_message,
		"ip_zero": Ivrdata.ip_zero,
		"ip_one": Ivrdata.ip_one,
		"ip_two": Ivrdata.ip_two,
		"ip_three": Ivrdata.ip_three,
		"ip_four": Ivrdata.ip_four,
		"ip_five": Ivrdata.ip_five,
		"ip_six": Ivrdata.ip_six,
		"ip_seven": Ivrdata.ip_seven,
		"ip_eight": Ivrdata.ip_eight,
		"ip_nine": Ivrdata.ip_nine,
		"ivr_id" : Ivrdata.id,
		"user_id" :Ivrdata.user_id
	}


	if request.method == 'POST':
		form = ConfigIvrForm(request.POST)
		Ivrdata.ivr_name = request.POST['ivr_name']
		Ivrdata.ivr_message = request.POST['welcome_message']
		Ivrdata.ivr_no_input_message = request.POST['no_input_message']
		Ivrdata.ivr_wrong_input_message = request.POST['wrong_input_message']
		Ivrdata.ip_zero = request.POST['zeroip_message']  if (request.POST['zeroip_message']!='') else 'Invalid Input'
		Ivrdata.ip_one = request.POST['oneip_message']  if (request.POST['oneip_message']!='') else 'Invalid Input'
		Ivrdata.ip_two = request.POST['twoip_message']  if (request.POST['twoip_message']!='') else 'Invalid Input'
		Ivrdata.ip_three = request.POST['threeip_message']  if (request.POST['threeip_message']!='') else 'Invalid Input'
		Ivrdata.ip_four = request.POST['fourip_message']  if (request.POST['fourip_message']!='') else 'Invalid Input'
		Ivrdata.ip_five = request.POST['fiveip_message']  if (request.POST['fiveip_message']!='') else 'Invalid Input'
		Ivrdata.ip_six = request.POST['sixip_message']  if (request.POST['sixip_message']!='') else 'Invalid Input'
		Ivrdata.ip_seven = request.POST['sevenip_message']  if (request.POST['sevenip_message']!='') else 'Invalid Input'
		Ivrdata.ip_eight = request.POST['eightip_message']  if (request.POST['eightip_message']!='') else 'Invalid Input'
		Ivrdata.ip_nine = request.POST['nineip_message']  if (request.POST['nineip_message']!='') else 'Invalid Input'
		Ivrdata.save()

		return HttpResponseRedirect('/response/ivr/list/')
	print Ivrdata.id, Ivrdata.ivr_message
	return render(request, "ivr_edit.html", context)


def ivr_delete(request, ivr_id, user_id):
	Ivrdata = IvrData.objects.get(id=ivr_id)
	Ivrdata.delete()
	return HttpResponseRedirect('/response/ivr/list/')

def ivr_endpoint(request, ivr_id, user_id):
	print ivr_id, user_id
	Ivrdata = IvrData.objects.get(id=ivr_id)
	print Ivrdata.ip_zero , Ivrdata.ip_one
	#Ivrdata = Ivrdata.filter(id=ivr_id)
	context = {
		"working": "yes"
	}

	print Ivrdata.id, Ivrdata.ivr_name, Ivrdata.ivr_message

	response = plivoxml.Response()
	if request.method == 'GET':
		print request.get_host(), request.build_absolute_uri()
		getdigits_action_url = request.build_absolute_uri()
		getDigits = plivoxml.GetDigits(action=getdigits_action_url, method='POST', timeout=7, numDigits=1, retries=1)
		#getDigits.add('{% csrf_token %}')
		getDigits.addSpeak(Ivrdata.ivr_message)
		response.add(getDigits)
		response.addSpeak(Ivrdata.ivr_no_input_message)
		return HttpResponse(response, content_type="text/xml")

	elif request.method == 'POST':
		#digit = request.POST['Digits']
		digit = request.form.get('Digits')
		print digits

		if (digit == "0" or digit == 0):
			response.addSpeak(Ivrdata.ip_zero)
		elif (digit == "1" or digit == 1):
			response.addSpeak(Ivrdata.ip_one)
		elif (digit == "2" or digit == 2):
			response.addSpeak(Ivrdata.ip_two)
		elif (digit == "3" or digit == 3):
			response.addSpeak(Ivrdata.ip_three)
		elif (digit == "4" or digit == 4):
			response.addSpeak(Ivrdata.ip_four)
		elif (digit == "5" or digit == 5):
			response.addSpeak(Ivrdata.ip_five)
		elif (digit == "6" or digit == 6):
			response.addSpeak(Ivrdata.ip_six)
		elif (digit == "7" or digit == 7):
			response.addSpeak(Ivrdata.ip_seven)
		elif (digit == "8" or digit == 8):
			response.addSpeak(Ivrdata.ip_eight)
		elif (digit == "9" or digit == 9):
			response.addSpeak(Ivrdata.ip_nine)
		else:
			response.addSpeak(WRONG_INPUT_MESSAGE)

		return HttpResponse(response, content_type="text/xml")
	
def ivr_sample(request):
	context = {
		"working": "yes"
	}
	response = plivoxml.Response()
	if request.method == 'GET':
		print request.get_host(), request.build_absolute_uri()
		getdigits_action_url = request.build_absolute_uri()
		getDigits = plivoxml.GetDigits(action=getdigits_action_url, method='POST', timeout=7, numDigits=1, retries=1)
		#getDigits.add('{% csrf_token %}')
		getDigits.addSpeak("Welcome to Sample IVR, Press 0 for sales , Press 1 for support")
		response.add(getDigits)
		response.addSpeak("Sorry No Input has been received")
		digit = request.POST['Digits']
		#digit = request.form.get('Digits')
		

		if (digit == "0" or digit == 0):
			response.addSpeak("Hello Welcome to Sample , I am a Sales Guy")
		elif (digit == "1" or digit == 1):
			response.addSpeak("Hello Welcome to Sample , I am a Support Guy")
		else:
			response.addSpeak("Wrong Input Received")
		return HttpResponse(response, content_type="text/xml")

	elif request.method == 'POST':
		digit = request.POST['Digits']
		#digit = request.form.get('Digits')
		

		if (digit == "0" or digit == 0):
			response.addSpeak("Hello Welcome to Sample , I am a Sales Guy")
		elif (digit == "1" or digit == 1):
			response.addSpeak("Hello Welcome to Sample , I am a Support Guy")
		else:
			response.addSpeak("Wrong Input Received")

		return HttpResponse(response, content_type="text/xml")
