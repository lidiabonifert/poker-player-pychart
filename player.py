import json
import sys


class Player:
    VERSION = "Error check"

    def get_self(self, current_game):
        for i in range(0, len(current_game["players"])):
            if current_game["players"][i]["name"] == "PyChart":
                return current_game["players"][i]

    def get_cards(self, self_data):
        first_card = self_data["hole_cards"][0]
        second_card = self_data["hole_cards"][1]
        return first_card, second_card

    def get_stack(self, self_data):
        return self_data["stack"]

    def betRequest(self, game_state):
        sys.stderr.write(game_state)
        current_game = game_state  # json.loads(game_state)
        self_data = get_self(current_game)
        current_stack = get_stack(self_data)
        received_hand = get_cards(self_data)
        if received_hand[0]["rank"] == received_hand[1]["rank"]:
            return current_stack
        return 0

    def showdown(self, game_state):
        pass
