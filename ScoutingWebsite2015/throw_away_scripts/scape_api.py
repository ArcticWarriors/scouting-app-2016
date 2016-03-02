'''
Created on Feb 28, 2016

@author: PJ
'''

#############################################################
# Load django settings so this can be run as a one-off script
#############################################################
import os
import sys

from django.core.wsgi import get_wsgi_application


os.environ["DJANGO_SETTINGS_MODULE"] = "ScoutingWebsite.settings"
proj_path = os.path.abspath("..")
sys.path.append(proj_path)
application = get_wsgi_application()

#############################################################

import json
from urllib2 import Request, urlopen

from Scouting2016.models import OfficialMatch, Team
from throw_away_scripts.api_key import get_encoded_key


__api_website = "https://frc-api.firstinspires.org/v2.0/"


def read_url_and_dump(url, headers, output_file):
    request = Request(url, headers=headers)
    response_body = urlopen(request).read()

    json_struct = json.loads(response_body)

    with open(output_file, 'w') as f:
        json.dump(json_struct, f, indent=4, separators=(',', ': '))

    return json_struct


def read_local_copy(input_file):
    with open(input_file, 'r') as f:
        response_body = f.read()

    json_struct = json.loads(response_body)

    return json_struct


def scrape_schedule(event_code, start):
    tourny_level = "Qualification"

    url = __api_website + "/2016/schedule/{0}?tournamentLevel={1}&start={2}".format(event_code, tourny_level, start)

    headers = {}
    headers['Accept'] = 'application/json'
    headers['Authorization'] = 'Basic ' + get_encoded_key()

    local_file = '__temp_schedule_query.json'
#     json_struct = read_url_and_dump(url, headers, local_file)
    json_struct = read_local_copy(local_file)

    schedule_info = json_struct["Schedule"]

    for match_info in schedule_info:
        match_number = match_info["matchNumber"]

        red_teams = []
        blue_teams = []

        for team_info in match_info["Teams"]:
            team, _ = Team.objects.get_or_create(teamNumber=team_info["teamNumber"])
            if "Red" in team_info["station"]:
                red_teams.append(team)
            else:
                blue_teams.append(team)

        official_search = OfficialMatch.objects.filter(matchNumber=match_number)
        if len(official_search) == 0:
            official_match = OfficialMatch.objects.create(matchNumber=match_number,
                                                          redTeam1=red_teams[0],
                                                          redTeam2=red_teams[1],
                                                          redTeam3=red_teams[2],
                                                          blueTeam1=blue_teams[0],
                                                          blueTeam2=blue_teams[1],
                                                          blueTeam3=blue_teams[2])
        else:
            official_match = official_search[0]
            official_match.redTeam1 = red_teams[0]
            official_match.redTeam2 = red_teams[1]
            official_match.redTeam3 = red_teams[2]
            official_match.blueTeam1 = blue_teams[0]
            official_match.blueTeam2 = blue_teams[1]
            official_match.blueTeam3 = blue_teams[2]
            official_match.save()

        print match_number, red_teams, blue_teams


def scrape_match_results(event_code, start):
    tourny_level = "Qualification"
    season = "2016"

    url = __api_website + "/{0}/scores/{1}/{2}?start={3}".format(season, event_code, tourny_level, start)
    headers = {'Accept': 'application/json'}
    headers['Authorization'] = 'Basic ' + get_encoded_key()

    local_file = '__temp_scoreresult_query.json'
#     json_struct = read_url_and_dump(url, headers, local_file)
    json_struct = read_local_copy(local_file)

    scores_info = json_struct["MatchScores"]
    for match_info in scores_info:
        match_number = match_info["matchNumber"]
        audience_defense = match_info["AudienceGroup"][-1]

        official_match = OfficialMatch.objects.get(matchNumber=match_number)
        official_match.audienceSelectionCategory = audience_defense

        for alliance_info in match_info["Alliances"]:
            color = alliance_info["alliance"]
            if color == "Red":
                official_match.redAutoBouldersLow = alliance_info["autoBouldersLow"]
                official_match.redAutoBouldersHigh = alliance_info["autoBouldersHigh"]
                official_match.redTeleBouldersLow = alliance_info["teleopBouldersLow"]
                official_match.redTeleBouldersHigh = alliance_info["teleopBouldersHigh"]
                official_match.redTowerFaceA = alliance_info["towerFaceA"]
                official_match.redTowerFaceB = alliance_info["towerFaceB"]
                official_match.redTowerFaceC = alliance_info["towerFaceC"]
                official_match.redFouls = alliance_info["foulCount"]
                official_match.redTechFouls = alliance_info["techFoulCount"]
            elif color == "Blue":
                official_match.blueAutoBouldersLow = alliance_info["autoBouldersLow"]
                official_match.blueAutoBouldersHigh = alliance_info["autoBouldersHigh"]
                official_match.blueTeleBouldersLow = alliance_info["teleopBouldersLow"]
                official_match.blueTeleBouldersHigh = alliance_info["teleopBouldersHigh"]
                official_match.blueTowerFaceA = alliance_info["towerFaceA"]
                official_match.blueTowerFaceB = alliance_info["towerFaceB"]
                official_match.blueTowerFaceC = alliance_info["towerFaceC"]
                official_match.blueFouls = alliance_info["foulCount"]
                official_match.blueTechFouls = alliance_info["techFoulCount"]
            else:
                print "OH NOES!"

        official_match.save()


event_code = "SCMB"
match_start = 0

scrape_schedule(event_code, match_start)
scrape_match_results(event_code, match_start)
