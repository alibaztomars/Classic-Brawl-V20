from os import truncate
from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class PlayerProfileMessage(Writer):

    def __init__(self, client, player, high_id, low_id, acc_data):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.high_id = high_id
        self.low_id = low_id
        self.acc_data = acc_data

    def encode(self):
        for i in range(2):#using this just to do not waste time fixing spaces :/
            if self.low_id == self.acc_data["ID"]:
                self.UnlockedBrawlersList = []
                for brawler_id in self.acc_data["UnlockedBrawlers"]:
                    if self.acc_data["UnlockedBrawlers"][str(brawler_id)] == 1:
                        self.UnlockedBrawlersList.append(int(brawler_id))

                self.writeVint(self.high_id)  # High Id
                self.writeVint(self.low_id)  # Low Id
                self.writeVint(0)  # Unknown

                self.writeVint(len(self.UnlockedBrawlersList))  # Brawlers array

                for brawler_id in self.UnlockedBrawlersList:
                    self.writeScId(16, int(brawler_id))
                    self.writeVint(0)
                    self.writeVint(self.acc_data["brawlersTrophiesForRank"][str(brawler_id)])  # Trophies for rank
                    self.writeVint(self.acc_data["brawlersTrophies"][str(brawler_id)])  # Trophies
                    self.writeVint(self.acc_data["brawlerPowerLevel"][str(brawler_id)])  # power lvl

                self.writeVint(15)

                self.writeVint(1)
                self.writeVint(self.acc_data["3vs3Wins"])  # 3v3 victories

                self.writeVint(2)
                self.writeVint(self.acc_data["playerExp"])  # Player experience

                self.writeVint(3)
                self.writeVint(self.acc_data["trophies"])  # Trophies

                self.writeVint(4)
                self.writeVint(self.acc_data["highesttrophies"])  # Highest trophies

                self.writeVint(5)
                self.writeVint(len(self.UnlockedBrawlersList))  # Brawlers list

                self.writeVint(7)
                self.writeVint(28000000 + self.acc_data["profileIcon"])  # Profile icon??

                self.writeVint(8)
                self.writeVint(self.acc_data["soloWins"])  # Solo victories

                self.writeVint(9)
                self.writeVint(794)  # Best robo rumble time

                self.writeVint(10)
                self.writeVint(794)  # Best time as big brawler

                self.writeVint(11)
                self.writeVint(self.acc_data["duoWins"])  # Duo victories

                self.writeVint(12)
                self.writeVint(20)  # Highest boss fight lvl passed

                self.writeVint(13)
                self.writeVint(1246)  # Highest power player points

                self.writeVint(14)
                self.writeVint(1)  # Highest power play rank

                self.writeVint(15)
                self.writeVint(15)  # most challenge wins

                self.writeVint(16)
                self.writeVint(20)

                self.writeString(self.acc_data["name"])
                self.writeVint(100)
                self.writeVint(28000000 + self.acc_data["profileIcon"])  # Profile icon
                self.writeVint(43000000 + self.acc_data["namecolor"])  # Name color

                if self.acc_data["clubID"] != 0:
                    DataBase.loadClub(self, self.acc_data["clubID"])

                    self.writeBoolean(True)  # Is in club

                    self.writeInt(0)
                    self.writeInt(self.acc_data["clubID"])
                    self.writeString(self.clubName)  # club name
                    self.writeVint(8)
                    self.writeVint(self.clubbadgeID)  # Club badgeID
                    self.writeVint(self.clubtype)  # club type | 1 = Open, 2 = invite only, 3 = closed
                    self.writeVint(self.clubmembercount)  # Current members count
                    self.writeVint(self.clubtrophies)
                    self.writeVint(self.clubtrophiesneeded)  # Trophy required
                    self.writeVint(0)  # (Unknown)
                    self.writeString(self.clubregion)  # region
                    self.writeVint(0)  # (Unknown)
                    self.writeVint(0)  # (Unknown)
                    self.writeVint(25)
                    self.writeVint(self.acc_data["clubRole"])
                else:
                    self.writeVint(0)
                    self.writeVint(0)