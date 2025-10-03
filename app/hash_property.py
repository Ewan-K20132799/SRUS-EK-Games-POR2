import app.player_node
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

class Player_hash_method:

    def __init__(self):
        self.SIZE = PlayerList.size
        self.key = app.player_node.key_uid
        self.uid = app.player.Player.uid

    @classmethod
    def player_hash_function(cls, key: str) -> int:
        player_h = [PlayerNode(key.uid)] % cls.SIZE
        return hash(player_h)


