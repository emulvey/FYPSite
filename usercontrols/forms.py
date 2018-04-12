from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email',)
	
	def clean(self):
		data = self.cleaned_data
		password = data["password"]
		confirm_password = data["confirm_password"]
		if password != confirm_password:
			raise forms.ValidationError("passwords do not match")
			
		email = data["email"]
		
		username = data["username"]
		test = User.objects.filter(username=username).exists()
		
		if test:
			raise forms.ValidationError("username already in use")
		
		return data
		

class LoginForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username',)
	
	def clean(self):
		data = self.cleaned_data
		password = data["password"]
		confirm_password = data["confirm_password"]
		if password != confirm_password:
			raise forms.ValidationError("passwords do not match")
		
		test1 = User.objects.filter(password=password).exists()
		if not test1:
			raise forms.ValidationError("incorrect password")
		
		username = data["username"]
		test2 = User.objects.filter(username=username).exists()
		if not test2:
			raise forms.ValidationError("username does not exist")
		
		return data