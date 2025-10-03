import unittest

import app.player

import app.player_list

import app.hash

import app.hash_property


class TestPlayerHashMap(unittest.TestCase):

    def test_get_item(self):
        if app.hash.PlayerHashMap == hash(app.hash.PlayerHashMap.key):
            return hash(app.hash.PlayerHashMap.key)
        else:
            return f"{ValueError or TypeError} get has failed."

    def test_set_item(self):
        if app.hash.PlayerHashMap.__setitem__ == app.hash.PlayerHashMap.__setitem__:
            if app.hash.PlayerHashMap.__setitem__ == app.hash.PlayerHashMap.changed_n:
                return app.hash.PlayerHashMap.__setitem__
            else:
                return app.hash.PlayerHashMap.__setitem__
        else:
            return f"{ValueError or TypeError} set has failed."

    def test_del_item(self):
        if app.hash.LinkedPlayerNode is self:
            return app.hash.LinkedPlayerNode.pop_node(app.hash.PlayerHashMap.key.uid)
        else:
            return f"{ValueError or TypeError} get has failed."

    def test_new_hash(self):
        if hash.__hash__ == app.hash.PlayerHashMap.__hash__:
            return app.hash.PlayerHashMap.__hash__
        else:
            return f"{ValueError or TypeError} get has failed."


    def test_hash_display(self):
        if app.hash.PlayerHashMap.display == print(f"{app.hash.PlayerHashMap.key}, "
                                                   f"{app.hash.PlayerHashMap.name}"):
            return True
        else:
            return False