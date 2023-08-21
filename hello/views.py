import json

from django.shortcuts import render

from .models import Greeting, Player

import os
from django.http import HttpResponse
# Create your views here.

from hello.ts_modules.Usta import getPlayers


def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('Hello!' * times)


def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



def api(request):
    page = request.headers['Page']
    res = getPlayers(page)
    playersList = json.loads(res)
    for p in playersList:
        player = Player(last_name=p, first_name="", utr=0.00, info="info placeholder")
        player.save()
    players = list(Player.objects.all())
    last_names = []
    for p in players:
        last_names.append(p.last_name)
    return HttpResponse(json.dumps(last_names))

