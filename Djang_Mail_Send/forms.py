from django import forms
from .models import universitydb, Postxx


class RegForm(forms.Form):
	
	Name = forms.CharField(
		#widget=forms.Textarea,
		min_length=5,
		error_messages={
			'required': 'Please enter your name',
			'min_length': 'Please write at least 300 characters (you have written %(show_value)s)'
		}
	)
	
	
	Role = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your role no.',
			'min_length': 'Please write at least 300 characters (you have written %(show_value)s)'
		}
	)
	
	DOB = forms.CharField(
		#widget=forms.Textarea,
		min_length=5,
		error_messages={
			'required': 'Please enter your name',
			'min_length': 'Please write at least 5 characters (you have written %(show_value)s)'
		}
	)
	
	
	Mobile = forms.CharField(
		#widget=forms.Textarea,
		min_length=8,
		error_messages={
			'required': 'Please enter your mobile no',
			'min_length': 'Please write at least 8 characters (you have written %(show_value)s)'
		}
	)
	
	
class LoginForm(forms.Form):
	
	User = forms.CharField(
		#widget=forms.Textarea,
		min_length=5,
		error_messages={
			'required': 'Please enter your user-id',
			'min_length': 'Please write at least 5 characters (you have written %(show_value)s)'
		}
	)
	
	
	Password = forms.CharField(
		#widget=forms.Textarea,
		min_length=3,
		error_messages={
			'required': 'Please enter your password.',
			'min_length': 'Please write at least 3 characters (you have written %(show_value)s)'
		}
	)	

class PrintForm(forms.Form):
	
	myprint = forms.CharField(
		#widget=forms.Textarea,

	)
	
class PostxxForm(forms.ModelForm):
    class Meta:
		model = Postxx
		fields = ['title']
        #exclude = ()
	
