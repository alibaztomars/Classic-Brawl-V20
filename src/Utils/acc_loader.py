from Database.DatabaseManager import DataBase
class acc_loader:
    def load(self, player_data):
    	self.player.name = player_data["name"]
    	self.player.low_id = player_data["ID"]
    	self.player.player_experience = player_data["playerExp"]
    	self.player.LowID = player_data["ID"]
    	self.player.Token = player_data["Token"]
    	self.player.solo_wins = player_data["soloWins"]
    	self.player.duo_wins = player_data["duoWins"]
    	self.player.ThreeVSThree_wins = player_data["3vs3Wins"]
    	self.player.gems = player_data["gems"]
    	self.player.gold = player_data["gold"]
    	self.player.star_points = player_data["starpoints"]
    	self.player.tickets = player_data["tickets"]
    	self.player.tokensdoubler = player_data["tokensdoubler"]
    	self.player.player_tokens = player_data["playerTokens"]
    	self.player.brawler_id = player_data["brawlerID"]
    	self.player.skin_id = player_data["skinID"]
    	self.player.profile_icon = player_data["profileIcon"]
    	self.player.brawl_boxes = player_data["brawlBoxes"]
    	self.player.big_boxes = player_data["bigBoxes"]
    	self.player.brawlers_skins = player_data["brawlersSkins"]
    	self.player.name_color = player_data["namecolor"]
    	self.player.starpower = player_data["starpower"]
    	self.player.DoNotDistrubMessage = player_data["DoNotDistrub"]
    	self.player.room_id = player_data["roomID"]
    	self.player.brawlers_trophies_in_rank = player_data["brawlersTrophiesForRank"]
    	self.player.brawlers_upgradium = player_data["brawlersUpgradePoints"]
    	self.player.Brawler_level = player_data["brawlerPowerLevel"]
    	self.player.brawlers_trophies = player_data["brawlersTrophies"]
    	if self.player.UnlockType == "Off":
    		self.player.BrawlersUnlockedState = player_data["UnlockedBrawlers"]
    	player_total_trophies = 0
    	for BrawlerID in self.player.brawlers_trophies.keys():
    	       player_total_trophies += self.player.brawlers_trophies[BrawlerID]
    	       self.player.trophies = player_total_trophies
    	       DataBase.replaceValue(self, 'trophies', self.player.trophies)
    	if self.player.trophies < player_data["highesttrophies"]:
    	       self.player.highest_trophies = player_data["highesttrophies"]
    	else:
    		self.player.highest_trophies = self.player.trophies