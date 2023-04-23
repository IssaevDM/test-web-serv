import sqlite3
import json
from attrs import define, field


# game_state JSON
# {
#     "stack": ["KH", "AH", "2H", "3C", "5D", "{A|K|Q|J|10 ... 2}{H|D|C|S}", "Last card must coincide with trump suite"],
#     "used_stack": ["Same as stack"],
#     "trump_suite": "{H|D|C|S}",
#     "table": [
#         {
#             "card": "",
#             "owner": "UUID"
#         }
#     ],
#     "attacker": "UUID",
#     "defender": "UUID",
#     "players": {
#         "UUID": {
#             "hand": ["not in stack or used stack"]
#         }
#     }
# }


@define(kw_only=True)
class Game:
    id = field()
    stack = field(init=False, factory=list)
    used_stack = field(init=False, factory=list)
    trump_suite = field(init=False, default="")
    table = field(init=False, factory=list)
    attacker = field(init=False, default=None)
    defender = field(init=False, default=None)
    players =  field(init=False, factory=dict)

    def saveState(self):
        with sqlite3.connect("durak.db") as sql3conn:
            with sql3conn.cursor() as cur:
                game_state = {
                    "stack": self.stack,
                    "used_stack": self.used_stack,
                    "trump_suite": self.trump_suite,
                    "table": self.table,
                    "attacker": self.attacker,
                    "defender": self.defender,
                    "players": self.players,
                }
                query = f"""insert into game_states (id, game_state) values ({self.id}, '{json.dumps(game_state)}') on conflict replace"""
                cur.execute(query)
            