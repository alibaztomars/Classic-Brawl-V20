from Logic.Player import Players
import json
#from tinydb import TinyDB, Query, database
from Logic.Player import Players
import json
import sys
#from tinydb import TinyDB, Query, database
from pymongo import MongoClient
with open("config.json", "r") as data:
	config = json.load(data)
from Database.MongoUtils import MongoUtils as db
cluster = MongoClient(config["mongodb_url"], serverSelectionTimeoutMS = 5000)
try:
	print("[DATABASE] Connecting to mongoDB cluster...")
	cluster.server_info()
except:
	print("[DATABASE] Failed to connect!")
	sys.exit()
print("[DATABASE] Succesfully connected to mongoDB cluster!")
datab = cluster["Classic-Brawl-V20"]
collection = datab["Players"]
gameroom_col = datab["Gamerooms"]
class DataBase:


    def loadAccount(self):
        token = self.player.token
        query = {"Token": token}
        result = db.load_document(collection, query)
        if result:
        	#print(result)
        	return result
    def loadAccountById(self, id):
        low_id = id
        query = {"ID": low_id}
        result = db.load_document(collection, query)
        if result:
        	#print(result)
        	return result

    def createAccount(self):
        Players.CreateNewBrawlersList()
       # db = TinyDB('Database/Player/data.db')

        data = {
                    "name": self.player.name,
                    "clubID": 0,
                    "clubRole": 0,
                    "isFBLinked": 0,
                    "facebookID": self.player.FacebookID,
                    "playerExp": self.player.player_experience,
                    "soloWins": self.player.solo_wins,
                    "duoWins": self.player.duo_wins,
                    "3vs3Wins": self.player.ThreeVSThree_wins,
                    "gems": self.player.gems,
                    "gold": self.player.gold,
                    "starpoints": self.player.star_points,
                    "tokensdoubler": self.player.tokensdoubler,
                    "playerTokens": self.player.player_tokens,
                    "tickets": self.player.tickets,
                    "brawlerID": 0,
                    "skinID": 0,
                    "trophies": self.player.trophies,
                    "highesttrophies": self.player.trophies,
                    "profileIcon": 0,
                    "namecolor": self.player.name_color,
                    "brawlBoxes": self.player.brawl_boxes,
                    "bigBoxes": self.player.big_boxes,
                    "starpower": 76,
                    "DoNotDistrub": 0,
                    "roomID": 0,
                    "brawlersSkins": self.player.brawlers_skins,
                    "brawlersTrophies": self.player.brawlers_trophies,
                    "brawlersTrophiesForRank": self.player.brawlers_trophies_in_rank,
                    "brawlersUpgradePoints": self.player.brawlers_upgradium,
                    "brawlerPowerLevel": self.player.Brawler_level,
                    "UnlockedBrawlers": self.player.BrawlersUnlockedState
        }
        auth = {
            "ID": self.player.low_id,
            "Token": self.player.token,
        }
        auth.update(data)
        db.insert_data(collection, auth)

       # db.insert(data)

    def getAllPlayers(self, args):
        result = db.load_all_documents_sorted(collection, {}, args)
        return result

        return name_list


    def replaceValue(self, item, value):
        token = self.player.token
        query = {"Token": token}
        db.update_document(collection, query, item, value)
    def gameroom(self):
    	query = {"room_id": self.player.room_id}
    	result = db.load_document(gameroom_col, query)
    	return result
    def loadGameroom(self):
        #db = TinyDB('Database/Gameroom/gameroom.db')
        #query = Query()
        #gameroom_data = db.search(query.room_id == self.player.room_id)
        roomID = self.player.room_id
        query = {"room_id": roomID}
        gameroom_data = db.load_document(gameroom_col, query)

        self.playersdata = {}
        if gameroom_data:
            self.mapID = gameroom_data["mapID"]
            self.playerCount = gameroom_data["PlayerCount"]
            self.playersdata[Players] = {}
            self.playersdata[Players]["IsHost"] = gameroom_data["host"]
            self.playersdata[Players]["name"] = gameroom_data["name"]
            self.playersdata[Players]["Team"] = gameroom_data["Team"]
            self.playersdata[Players]["Ready"] = gameroom_data["Ready"]
            self.playersdata[Players]["profileIcon"] = gameroom_data["profileIcon"]
            self.playersdata[Players]["namecolor"] = gameroom_data["namecolor"]
            self.playersdata[Players]["brawlerID"] = gameroom_data["brawlerID"]
            self.playersdata[Players]["starpower"] = gameroom_data["starpower"]
        #else:
           # playerdb = TinyDB('Database/Player/data.db')
            #query = Query()
           # data = playerdb.search(query.token == str(self.player.token))
           # player_data = DataBase.loadAccount(self)
            #user_data = player_data
            #player_data["roomID"] = 0
            #self.player.room_id = 0
            #playerdb.update(user_data, query.token == str(self.player.token))

    def replaceGameroomValue(self, value_name, new_value, type):
        #db = TinyDB('Database/Gameroom/gameroom.db')
        #query = Query()
        #valueToRemove = Query()
        #data = db.search(query.room_id == self.player.room_id)
        roomID = self.player.room_id
        query = {"room_id": roomID}
        gameroom_data = db.load_document(gameroom_col, query)

        if type == "room" or type == "player":
            #gameroom_data[str(value_name)] = new_value
            db.update_document(gameroom_col, query, value_name, new_value)
        #elif type == "player":
            #gameroom_data["info"][str(value_name)] = new_value
            #db.update(gameroom_data, query.room_id == self.player.room_id)
        elif type == "removePlayer":
        	db.delete_document(gameroom_col, query)
    def createGameroomDB(self):
       # db = TinyDB('Database/Gameroom/gameroom.db')
        data = { 
                "mapID": self.player.map_id,
                "PlayerCount": 1,
                    "host": 1,
                    "lowID": self.player.low_id,
                    "name": self.player.name,
                    "Team": self.player.team,
                    "Ready": self.player.isReady,
                    "brawlerID": self.player.brawler_id,
                    "starpower": self.player.starpower,
                    "profileIcon": self.player.profile_icon,
                    "namecolor": self.player.name_color
        }
        auth = {
            "room_id": self.player.room_id
        }
        auth.update(data)
        db.insert_data(gameroom_col, auth)
        #db.insert(data)
    
    def UpdateGameroomPlayerInfo(self, low_id):
       # db = TinyDB('Database/Gameroom/gameroom.db')
        query = {"room_id": self.player.room_id}
       # data = db.search(query.room_id == self.player.room_id)
        gameroom_data = db.load_document(gameroom_col, query)
        db.delete_document(gameroom_col, query)
        DataBase.createGameroomDB(self)
