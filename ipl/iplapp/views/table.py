from django.views import View
from iplapp.models import *
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import *
from django.db.models import *

class Table(View):
    def get(self,request,*args,**kwargs):
        curr=request.user
        user=curr.username
        season=kwargs["season"]
        teams=Matches.objects.values("team1").filter(season=kwargs['season']).distinct()
        teamsCount=len(teams)
        playoffs=Matches.objects.values("team1","team2","result","winner").filter(season=2017)[teamsCount*(teamsCount-1):]
        t=(teamsCount-1)*2
        points={}
        for i in teams:
            points[i["team1"]]=[]
            points[i["team1"]].append(len(Matches.objects.filter(season=kwargs['season'],winner=i["team1"]))*2)
            points[i["team1"]].append(points[i["team1"]][0]//2)
            points[i["team1"]][0] += len(Matches.objects.filter(season=kwargs['season'], team1=i["team1"],result="no result"))
            points[i["team1"]][0] += len(Matches.objects.filter(season=kwargs['season'], team2=i["team1"],result="no result"))
            points[i["team1"]].append(points[i["team1"]][0]-(points[i["team1"]][1]*2))
            for j in playoffs:
                if j["winner"]==i["team1"]:
                    points[i["team1"]][0]-=2
                    points[i["team1"]][1]-=1
                if (j["team1"]==i["team1"] or j["team2"]==i["team1"]) and j["result"]=="no result":
                    points[i["team1"]][0]-=1
                    points[i["team1"]][2]-=1
            points[i["team1"]].append(t - points[i["team1"]][1] + points[i["team1"]][2])
            points[i["team1"]].append(t)

        points = sorted(points.items(), key=lambda kv: -kv[1][0])
        return render(request,"table.html",{"points":points,"user":user,"season":season})
