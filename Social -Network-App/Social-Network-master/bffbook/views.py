from cmath import pi
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home_view(request):
    user = request.user
    hello = 'welcome back\nhello '+str(user) + " you are signed in"

    if str(user) == "AnonymousUser":
        hello = "_____________________This  is social networking app \n\t\t if you have an account,please sign in\n\t\tif you are new, you can create an account_________________"

    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'main/home.html', context)


def user_logout(request):
    logout(request)
    context = {
        'user': 'jojo dsd',
        'hello': "hello",
    }
    return render(request, 'main/home.html', context)


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'profiles/myprofile.html')
        ...
    else:
        # Return an 'invalid login' error message.
        print('invalid')
    # return HttpResponse('Hello world')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm

    success_url = '/accounts/login/?next=/profiles/myprofile/'
    template_name = "registration/signup.html"
