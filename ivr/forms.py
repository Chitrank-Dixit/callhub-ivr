from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password', 'password')


class SignedUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')

class ConfigIvrForm(forms.Form):
	ivr_message = forms.CharField()
	ivr_no_input_message = forms.Textarea()
	ivr_wrong_input_message = forms.Textarea()
	ip_zero = forms.CharField()
	ip_one = forms.CharField()
	ip_two = forms.CharField()
	ip_three = forms.CharField()
	ip_four = forms.CharField()
	ip_five = forms.CharField()
	ip_six = forms.CharField()
	ip_seven = forms.CharField()
	ip_eight = forms.CharField()
	ip_nine = forms.CharField()
	
#class GetDigitForm(forms.Form):

