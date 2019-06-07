import requests
import json
from .state import State




def call_api(state):
    print("call_api")

    url = 'http://localhost:8080/suggestMove'
    post_fields = "{\"Grid\":" + str(state.grid).replace(".","0") .replace("'","") + ", \"Piece\":" + str(state.game_turn.selected_piece) + "}"

    try:
        r = requests.post(url, data=post_fields)
        if r.status_code == 200:
            new_computer_state = json.loads(r.text)
            computer_piece = state.game_turn.selected_piece
            state.grid[new_computer_state["Move"][0]][new_computer_state["Move"][1]] = computer_piece
            state.remaining_pieces.remove(computer_piece)
            state.game_turn.selected_piece = new_computer_state["Piece"]
            return True
    except (TypeError, ValueError, UnboundLocalError):
        return False
    return False

