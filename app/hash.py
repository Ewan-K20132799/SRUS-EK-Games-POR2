from __future__ import annotations

from typing import Callable, Any
import app.hash_property
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode, LinkedPlayerNode
import app.player_node

class PlayerHashMap:   # initiation of hash map class
    changed_n = str
    SIZE = PlayerList.size
    key = app.player_node.key_uid
    uid = Player.uid
    name = Player.name
    hashmap: app.hash_property.Player_hash_method

    def __init__(self, hashmap: app.hash_property.Player_hash_method):
        _hashmap = hashmap

    def __hash__(self) -> int:
        hashmap = app.hash_property.Player_hash_method
        return hash(hashmap)

    def __getitem__(self, key: str | Player,
                    hashmap: app.hash_property.Player_hash_method) -> int | Exception:
        if isinstance(key.uid, PlayerNode):
            return hash(key.uid)
        else:
            is_not_instance = Exception(ValueError or TypeError)
            return is_not_instance
    def __setitem__(self,
                    key: str,
                    name: str | Player,
                    changed_n: str | Player,
                    index: str | Player) -> Callable[[], Any] | str | Player:

        if key in index:
            _name = changed_n.uid
            return changed_n.uid
        else:
            _name = name.uid
            return name

    def __len__(self, key: str,
                hashmap: int | app.hash_property.Player_hash_method) -> int:
        return hashmap

    def delete_item(self, key: str | Player,
                    name: str | Player,
                    changed_n: str | Player):
        if isinstance(key.uid, name.uid, changed_n.uid):
            LinkedPlayerNode._current_node = LinkedPlayerNode.current_node.prev_node
            LinkedPlayerNode._prev_node = LinkedPlayerNode._prev_node
            LinkedPlayerNode.pop_node(key.uid())
            return self
        elif not isinstance(key.uid, name.uid, changed_n.uid):
            return 'hash is not an instance.'
        else:
            return f'Error: {TypeError or ValueError}'

    def display(self,
                key: str | Player,
                name: str | Player,
                hashmap: str | app.hash_property.Player_hash_method):
     for key.uid, name.uid in hashmap % self.SIZE:
         print(f"{key.uid}, {name.uid}")