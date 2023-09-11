from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST': # fetch data from frontend and save in a variable
    	email = request.POST["email"]
    	password = request.POST["password"]
    	confirm_password = request.POST["Cpassword"]

    	if password == confirm_password: # validate passwords
    		if User.objects.filter(email=email).exists():
    			print('Username Taken')
    			messages.error(request, 'Email Already Taken!')
    			return render(request, 'signup.html')

    		else:
    			user = User.objects.create_user(username=email, password=password)
    			user.save();
    			auth.login(request, user) # Log in the user after registration
    			return redirect("hello_world") # Redirect to the "Hello World" page

    	else:
    		print('Password does not match')
    		messages.error(request, 'Password Does Not Match!')
    		return render(request, 'signup.html')

    return render(request, 'signup.html')


def login(request):
	if request.method == "POST":
		email = request.POST.get("email", None)
		password = request.POST.get("pass", None)

		user = auth.authenticate(username=email, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("hello_world")

		else:
			messages.error(request, 'Incorrect Email or Password!')
			return render(request, 'login.html')
	else:
		return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required
def hello_world(request):
    # view logic here
    return render(request, "hello_World.html")