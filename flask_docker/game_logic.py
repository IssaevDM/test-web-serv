import sqllite3
from attrs import define, field


@define(kw_only=True)
class Game:
    id = field()
    
    def saveState(self):
        with sqllite3.connect("durak.db") as sql3conn:
            with sql3conn.cursor() as cur:
                

        sqllite3.