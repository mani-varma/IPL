from django.urls import path
from iplapp.views import *

patterns=[
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', logout_user, name="logout"),

    path("season/",season.as_view(),name="s"),
    path("season/<int:season>/",season.as_view(),name="season"),
    path("season/<int:season>/<int:mid>/",match.as_view(),name="match"),

    path("season/<int:mid>/innings/<int:innings>/", innings.as_view(), name="inning"),

    path("table/<int:season>/",Table.as_view(),name="table"),

    path("team/<str:name>/",Team.as_view(),name="table"),

]