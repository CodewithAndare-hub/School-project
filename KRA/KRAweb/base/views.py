from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, template_name="base/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first = request.POST.get("first")
        second = request.POST.get("second")
        email = request.POST.get("email")
        DOB = request.POST.get("DOB")
        DOB_number = request.POST.get("DOB-number")
        id_number = request.POST.get("id")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        my_user = User.objects.create_user(username, id_number, pass1)
        my_user.fname = first
        my_user.sname = second
        my_user.DOB = DOB

        my_user.save()
        messages.success(request, message="Account created successfully")
        return redirect("signin")

    return render(request, template_name="base/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        id_number = request.POST.get("id")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, template_name="base/index.html")
        else:
            messages.error(request, message="Wrong details provided")
            return render(request, template_name="base/signin.html")
    return render(request, template_name="base/signin.html")

def sign_out(request):
    pass


