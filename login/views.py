from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from .models import User
from django.contrib import messages


def login(request):

    return render(request, "login.html")

def new_user(request):
    errors = User.objects.basic_validator(request.POST)

    user = User.objects.filter(email = request.POST["email"])
    if user:
        messages.error(request, "Email is already in use")

    elif len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/login/")
    
    else: 
        hash1 = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], email = request.POST["email"], company_name = request.POST["company_name"],  password = hash1)
        request.session["user_id"] = new_user.id
        return redirect("/form")

def validateLogin(request):
    user = User.objects.filter(email = request.POST["email"])
    if not user:
        messages.error(request, "User not found")
        return redirect("/login/")
    
    else:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST["password"].encode(), logged_user.password.encode()):
            request.session["user_id"] = logged_user.id
            return redirect("/form")

        else: 
            messages.error(request, "password is not correct")
        return redirect("/login/")
