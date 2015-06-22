import os
from django.shortcuts import render, render_to_response

# Django Authentication builtins
from django.contrib import auth
from django.contrib.auth import login , logout
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponse , HttpRequest
# our django forms
from forms import UserForm , SignedUserForm, ConfigIvrForm

# importing models
from models import IvrData

from django.template import RequestContext
# sending mail usin Django
from django.core.mail import send_mail
import plivoxml
from utils import joke_from_reddit


def home(request):
	title = "Welcome"
	# if request.user.is_authenticated():
	# 	title = "My Title %s" % (request.user)
	# add a form

	# form = SignUpForm(request.POST or None)
	context = {
		"template_title": title,
	 	#"form": form
	}
	# if request.method == "POST":
	# 	print "Hii",request.POST['email'], request.POST['full_name'] # ,request.POST.email, request.POST.full_name
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	instance.save()
	# 	print instance.email, instance.timestamp
	# 	context = {
	# 		"template_title": "Thank You"
	# 	}
		
	return render(request ,"index.html",context)

def login(request):
	title = "Login"
	context = {
		"template_title": title,
	 	#"form": form
	}
	print "Heeee"
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request,user)
			return HttpResponseRedirect('/')
			#return render_to_response('index.html',{}, context_instance=RequestContext(request))# HttpResponseRedirect('/blog/profile/')  '/blog/profile/'
		elif user is None:
			print 'hii'
			#return HttpResponseRedirect('/login')
			#return render_to_response('index.html',{}, context_instance=RequestContext(request))# HttpResponseRedirect('home')  # '/blog/home/'
	return render(request ,"login.html",context)


def register(request):
	title = "Register"
	send_email=''
	print "Heeee"
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			new_user.save()
			new_user.backend='django.contrib.auth.backends.ModelBackend'
			auth.login(request,new_user)
			# send_email=request.POST.get('email')
			# redirect, or however you may want to get to the main view
			return HttpResponseRedirect('/')
		else:
			form = UserForm()

	#send_mail('Subject here', 'Here is the message.', 'chitrankdixit@gmail.com',
	#[send_email], fail_silently=False)
	context = {
	    "template_title": title,
	    #"form": form
	}
	return render(request ,"register.html",context)

def signout(request):
    logout(request)
    context = {}
    return render(request, "index.html",context)

# This file will be played when a caller presses 2.
PLIVO_SONG = "https://s3.amazonaws.com/plivocloud/music.mp3"

# This is the message that Plivo reads when the caller dials in
IVR_MESSAGE = "Welcome to the Callhub IVR Demo App. Press 1 to hear a random \
                joke. Press 2 to listen to a song."

# This is the message that Plivo reads when the caller does nothing at all
NO_INPUT_MESSAGE = "Sorry, I didn't catch that. Please hangup and try again \
                    later."

# This is the message that Plivo reads when the caller inputs a wrong number.
WRONG_INPUT_MESSAGE = "Sorry, it's wrong input."


def ivr_view(request):
	response = plivoxml.Response()
	if request.method == 'GET':
		print request.get_host()
		getdigits_action_url = 'http://'+request.get_host() + '/response/ivr/' #url_for('ivr', _external=True)
		getDigits = plivoxml.GetDigits(action=getdigits_action_url, method='POST', timeout=7, numDigits=1, retries=1)
		getDigits.addSpeak(IVR_MESSAGE)
		response.add(getDigits)
		response.addSpeak(NO_INPUT_MESSAGE)
		return HttpResponse(str(response), content_type="text/xml")
	elif request.method == 'POST':
		digit = request.POST['Digits']

		if digit == "1":
			response.addSpeak("")
		elif digit == "2":
			response.addPlay(PLIVO_SONG)
		else:
			response.addSpeak(WRONG_INPUT_MESSAGE)

		return HttpResponse(str(response), content_type="text/xml")


def config_ivr(request):
	context = {
		"template_title": "Configure IVR"
	}
	print 'hii'
	if request.method == 'POST':
		form = ConfigIvrForm(request.POST)
		configure_ivr = IvrData()
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

		return HttpResponseRedirect('/')
		# if form.is_valid():
		# 	print "hii2"
		# 	instance = form.save(commit=False)
		# 	print form.cleaned_data.get("welcome_message")
		# 	instance.save();
	return render(request,"config_ivr.html", context)

def ivrs(request):
	Ivrdata = IvrData.objects.all()
	context = {
		# "template_title": {{request.user.username}} + "IVRs",
		"ivrdata": Ivrdata
	}	
	return render(request, "list_ivrs.html", context)

# @app.route('/response/ivr/', methods=['GET', 'POST'])
# def ivr():
#     response = plivoxml.Response()
#     if request.method == 'GET':
#         # GetDigit XML Docs - http://plivo.com/docs/xml/getdigits/
#         getdigits_action_url = url_for('ivr', _external=True)
#         getDigits = plivoxml.GetDigits(action=getdigits_action_url,
#                                        method='POST', timeout=7, numDigits=1,
#                                        retries=1)

#         getDigits.addSpeak(IVR_MESSAGE)
#         response.add(getDigits)
#         response.addSpeak(NO_INPUT_MESSAGE)

#         return Response(str(response), mimetype='text/xml')

#     elif request.method == 'POST':
#         digit = request.form.get('Digits')

#         if digit == "1":
#             # Fetch a random joke using the Reddit API.
#             joke = joke_from_reddit()
#             response.addSpeak(joke)
#         elif digit == "2":
#             # Listen to a song
#             response.addPlay(PLIVO_SONG)
#         else:
#             response.addSpeak(WRONG_INPUT_MESSAGE)

#         return Response(str(response), mimetype='text/xml')
