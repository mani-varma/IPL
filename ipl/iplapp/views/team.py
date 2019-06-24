from django.views import View
from iplapp.models import *
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import *
from django.db.models import *

class Team(View):
    def get(self,request,*args,**kwargs):
        curr = request.user
        user = curr.username
        seasons=Matches.objects.values("season").distinct().order_by('season')
        details=[]
        stats=[]
        stats.append(Matches.objects.filter(Q(team1=kwargs["name"])|Q(team2=kwargs["name"])).count())
        stats.append(Matches.objects.filter((Q(team1=kwargs["name"])|Q(team2=kwargs["name"]))&Q(winner=kwargs["name"])).count())
        stats.append(Matches.objects.filter((Q(team1=kwargs["name"])|Q(team2=kwargs["name"]))&Q(result="no result")).count())
        stats.append(stats[0]-(stats[1]+stats[2]))
        for year in seasons:
            details.append(Matches.objects.values("season","mid","team1", "team2","toss_winner","toss_decision","result","winner","player_of_match").filter(Q(season=year["season"]) & (Q(team1=kwargs["name"]) | Q(team2=kwargs["name"]))))
        return render(request,"team.html",{"Team":kwargs["name"],"details":details,"user":user,"stats":stats})