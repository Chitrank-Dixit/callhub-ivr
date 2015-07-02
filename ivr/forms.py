from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from models import IvrData

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password', 'password')


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')

class ConfigIvrForm(forms.ModelForm):
	class Meta:
		model = IvrData
		fields = ('ivr_name','ivr_message','ivr_no_input_message','ivr_wrong_input_message','ip_zero','ip_one','ip_two','ip_three','ip_four','ip_five','ip_six','ip_seven','ip_eight','ip_nine')
	
	
#class GetDigitForm(forms.Form):

