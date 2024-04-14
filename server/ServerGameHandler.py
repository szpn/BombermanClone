class ServerGameHandler:
    def __init__(self, map_name, num_players):
        self.map_name = map_name
        self.num_players = num_players
        self.players = []
        self.game = None

    def handle_message(self, message):
        if "id" in message:
            if message["id"] == "JOIN":
                if len(self.players) < self.num_players:
                    self.players.append(message["player"])
                    if len(self.players) == self.num_players:
                        self.start_game()

    def start_game(self):
        pass

    def update_game_state(self, game_state):
        pass