from django.contrib.auth import authenticate,login as Login,logout
from django.contrib import messages
from django.views import View
from iplapp.models import *
from django.shortcuts import *
from iplapp.forms import *
from django.urls import *
from django.contrib.auth.models import User

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=login.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        user=authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            Login(request,user)
            name = user.username
            season=2019
            matches = Matches.objects.filter(season=2019)
            return render(request, "seasons.html", {"matches": matches, "user": name,"season":season})

        else:
            messages.error(request,"Invalid Credentials")
            form=LoginForm(request.POST)
            return render(request,"login.html",{"form":form})


class SignUp(View):
    def get(self,request,*args,**kwargs):
        form=login.SignupForm()
        return render(request,"signup.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=login.SignupForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(**form.cleaned_data)
            user.save()

            if user is not None:
                Login(request,user)
                name=user.username
                season=2019
                matches = Matches.objects.filter(season=2019)
                return render(request, "seasons.html", {"matches": matches, "user": name,"season":season})

def logout_user(request):
    logout(request)
    return redirect("s")