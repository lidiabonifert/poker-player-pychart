import json
# import sys


class Player:
    VERSION = "Error check"

    def get_cards(self, game_state):
        first_card = game_state["hole_cards"][0]
        second_card = game_state["hole_cards"][1]
        return first_card, second_card

    def get_stack(self, game_state):
        return game_state["stack"]

    def betRequest(self, game_state):
        print("*********************")
        print(game_state["players"])
            #print(game_state[i])
            
        # sys.stderr.write(game_state)
        # current_game = game_state  # json.loads(game_state)
        # self_data = get_self(current_game)
        # current_stack = get_stack(self_data)
        # received_hand = get_cards(self_data)
        # if received_hand[0]["rank"] == received_hand[1]["rank"]:
          #  return 1000
        return 1000

    def showdown(self, game_state):
        pass
