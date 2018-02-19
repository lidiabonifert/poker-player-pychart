import json
# import sys


class Player:   
    VERSION = "0.1"

    def get_self(self, game_state):
            for i in range(0, len(game_state["players"])):
                if game_state["players"][i]["name"] == "PyChart":
                    return game_state["players"][i]

    def get_cards(self, get_self):
        first_card = get_self["hole_cards"][0]
        second_card = get_self["hole_cards"][1]
        return first_card, second_card

    def get_stack(self, game_state):
        return game_state["stack"]

    def check_if_card_higher_than(card1, card2):
        if card["rank"] in "QKA" and card2["rank"] in "QKA":
            return True

    def betRequest(self, game_state):
        print("*********************")
        print(get_self["name"])
        self_data = Player.get_self(game_state)
        received_hand = Player.get_cards(self_data)
        print("self data:")
        print(self_data)
        first_card = received_hand[0]
        print("first card: ")
        print(first_card)
        second_card = received_hand[1]
        print("second card")
        print(second_card)
        if first_card["rank"] == second_card["rank"]:
            return 1000
        return 0

    def showdown(self, game_state):
        pass
