from django.views import View
from iplapp.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.db.models import *


class season(View):

    def get(self,request,*args,**kwargs):
        curr=request.user
        user=curr.username
        if kwargs:
            matches=Matches.objects.filter(season=kwargs['season'])
            season=kwargs['season']
        else:
            matches = Matches.objects.filter(season=2019)
            season=2019
        return render(request, "seasons.html", {"matches": matches,"user":user,"season":season})


class match(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self,request,*args,**kwargs):
        curr = request.user
        user = curr.username

        match=Matches.objects.filter(mid=kwargs['mid'])[0]
        bat1 = Deliveries.objects.filter(mdid=match.mid,innings=1).values('batsman').annotate(runs=Sum('batsman_runs')).order_by("-runs")[:3]
        bat2 = Deliveries.objects.filter(mdid=match.mid,innings=2).values('batsman').annotate(runs=Sum('batsman_runs')).order_by("-runs")[:3]
        ball1=Deliveries.objects.filter(mdid=match.mid,innings=1).values('bowler').annotate(wickets=Count('player_dismissed'),runs=Sum('total_runs')).order_by("-wickets","runs")[:3]
        ball2=Deliveries.objects.filter(mdid=match.mid,innings=2).values('bowler').annotate(wickets=Count('player_dismissed'),runs=Sum('total_runs')).order_by("-wickets","runs")[:3]
        return render(request,"match.html",{"match":match,"bat1":bat1,"bat2":bat2,"ball1":ball1,"ball2":ball2,"user":user})

class innings(View):
    def get(self,request,*args,**kwargs):
        curr = request.user
        user = curr.username

        match=Matches.objects.filter(mid=kwargs['mid'])[0]
        if(kwargs['innings']==1):
            deliveries=Deliveries.objects.filter(mdid=match.mid,innings=1)
        else:
            deliveries = Deliveries.objects.filter(mdid=match.mid,innings=2)
        return render(request,"innings.html",{"deliveries":deliveries,"user":user})
