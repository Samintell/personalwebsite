from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

# Registration form modified from https://www.techwithtim.net/tutorials/django/user-registration/
def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("/home")
	else:
		form = RegisterForm()

	return render(response, "impostor/register.html", {"form":form, "title": "Register"})