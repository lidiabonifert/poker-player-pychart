
class Player:   
    VERSION = "0.1"

    def get_self(self, game_state):
            for player in game_state["players"]:
                print("------" + player + "------")
                if player["name"] == "PyChart":
                    return player

    def get_cards(self, get_self):
        first_card = get_self["hole_cards"][0]
        second_card = get_self["hole_cards"][1]
        return first_card, second_card

    def get_stack(self, game_state):
        return game_state["stack"]

    def check_if_card_higher_than(self, card1, card2):
        if (card1["rank"] in "QKA") and (card2["rank"] in "QKA"):
            return True

    def check_if_in_middle(self, card1, card2):
        return (card1["rank"] in "8910J") and (card2["rank"] in "8910J")

    def check_if_card_lower(self, card1, card2):
        return (card1["rank"] in "234567") and (card2["rank"] in "234567")

    def check_card_distance(self, card1, card2):
        return Player.check_if_card_lower(card1, card2) and (
                    max(int(card1["rank"]), int(card1["rank"])) - (min(int(card1["rank"]), int(card1["rank"]))) < 3)

    def check_if_same_color(self, card1, card2):
        return card1["suit"] == card2["suit"]


    def betRequest(self, game_state):
        print("*********************")
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
