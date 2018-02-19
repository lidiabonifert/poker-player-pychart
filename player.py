

class Player:
    VERSION = "All in!!"

    def betRequest(self, game_state):
        current_game = json.loads(game_state)
        for i in range(0, len(current_game[players])):
            if current_game[players][i][name] == "PyChart":
                first_rank = current_game[players][i][hole_cards][0][rank]
                second_rank = current_game[players][i][hole_cards][1][rank]
                if first_rank == second_rank:
                    return 100
        return 1000

    def showdown(self, game_state):
        pass
