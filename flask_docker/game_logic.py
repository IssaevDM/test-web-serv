import sqllite3
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
    
    def saveState(self):
        with sqllite3.connect("durak.db") as sql3conn:
            with sql3conn.cursor() as cur:
                query = f"""insert into games (id, game_state)"""
                cur.execute(query)