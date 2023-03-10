from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta(User):
		model = User
		fields = ['username', 'email', 'password1', 'password2']