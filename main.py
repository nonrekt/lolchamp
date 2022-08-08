from riotwatcher import LolWatcher, ApiError
import random
import json

from API_login import Login

api = Login()

watcher = api.lolwatcher


def convertIdToName(id):
    with open('champ_ids.json') as f:
        all_champion_id = json.load(f)

    return all_champion_id.get(str(id))


def selectFromAll(regionDragon):
    version = watcher.data_dragon.versions_for_region(regionDragon)
    champions_version = version['n']['champion']
    champList = watcher.data_dragon.champions(champions_version)
    champDicts = {}
    for champ in champList["data"]:
        champDicts[champList["data"][champ]["id"]] = champ
    champList = list(champDicts.values())
    return random.choice(champList)


def summonerId(region, summoner_name):
    data = watcher.summoner.by_name(region, summoner_name)
    return (data["id"])


def getMastery(region, summoner_name):
    id = summonerId(region, summoner_name)
    data = watcher.champion_mastery.by_summoner(region, id)
    return data


def printMasteryData(region, summoner_name):
    data = getMastery(region, summoner_name)
    level = 7
    choice = None
    while (level == 7):
        choice = random.choice(data)
        level = choice["championLevel"]
    id = choice["championId"]
    name = convertIdToName(id)
    level = choice["championLevel"]
    print(f" id: {id} \n name: {name} \n mastery level: {level}")


def mainMenu():
    print("1 -> Random champion \n2 ->  Random champion without mastery 7 \nquit -> exit")
    print()


def main():
    region = ""
    regionDragon = ""
    username = ""
    region_input = input("region: ")
    if (region_input == "eune"):
        regionDragon = "eune"
        region = "eun1"
    elif (region_input == "euw"):
        region, regionDragon = "euw1"
    username = input("username: ")
    userChoice = None
    while (userChoice != "quit"):
        mainMenu()
        userChoice = input("your choice: ")
        if (userChoice == "1"):
            print(selectFromAll(regionDragon))
        elif (userChoice == "2"):
            printMasteryData(region, username)
        else:
            continue
    quit()


if (__name__ == "__main__"):
    main()
