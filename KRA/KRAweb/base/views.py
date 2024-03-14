from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
import random
import string


def home(request):
    return render(request, template_name="base/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first = request.POST.get("first")
        second = request.POST.get("second")
        email = request.POST.get("email")
        dob = request.POST.get("DOB")
        dob_number = request.POST.get("DOB-number")
        id_number = request.POST.get("id")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        my_user = User.objects.create_user(username, email, pass1)

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
            username = user.username

            return render(request, template_name="base/kra-services.html", context={'username': username})
        else:
            messages.error(request, message="Wrong details provided")
            return render(request, template_name="base/signin.html")
    return render(request, template_name="base/signin.html")

def sign_out(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return render(request, template_name="base/index.html")

def about(request):
    return render(request, template_name="base/about.html")

def pin_generator(request):
    def generate_random_word(length=13):
        characters = string.ascii_uppercase + string.digits
        random_word = ''.join(random.choice(characters) for _ in range(length))
        return random_word

    pin = generate_random_word()

    return render(request, template_name="base/pin-generator.html", context={'kra_pin': pin})
def services(request):
    return render(request, template_name="base/services.html")

