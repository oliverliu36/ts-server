import json

from django.shortcuts import render

from .models import Greeting, Player

import os
from django.http import HttpResponse
# Create your views here.

from hello.ts_modules.Usta import getPlayers
from .ts_modules import UniversalTennis
from .ts_modules.processEntryList import get_new_players_list, look_up_players


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

    entry_list = json.loads(res)

    new_players = get_new_players_list(entry_list)

    if(len(new_players) > 0):
        UniversalTennis.runUniversalTennis(new_players)

    look_up_results = look_up_players(entry_list)

    return HttpResponse(json.dumps(look_up_results))

    # for p in entry_list:
    #     player = Player(last_name=p, first_name="", utr=0.00, info="info placeholder")
    #     player.save()
    # players = list(Player.objects.all())
    # last_names = []
    # for p in players:
    #     last_names.append(p.last_name)
    #
    # return HttpResponse(json.dumps(new_players))

