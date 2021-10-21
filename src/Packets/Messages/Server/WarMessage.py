from Utils.Writer import Writer


class WarMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24776
        self.player = player

    def encode(self):
        self.writeInt(0)
