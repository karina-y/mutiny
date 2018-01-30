from player import Player

class Action():
	def __init__(self, method, name, hotkeys, **kwargs):
		self.method = method
		self.hotkeys = hotkeys
		self.name = name
		self.kwargs = kwargs

	def __str__(self):
		#return "{}: {}".format(self.hotkeys, self.name)
		return "{}: {}".format(self.name, self.hotkeys)


class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=Player.move_north, name='Move north', hotkeys=['n', 'north'])


class MoveSouth(Action):
       def __init__(self):
                super().__init__(method=Player.move_south, name='Move south', hotkeys=['s', 'south'])


class MoveEast(Action):
       def __init__(self):
                super().__init__(method=Player.move_east, name='Move east', hotkeys=['e', 'east'])


class MoveWest(Action):
        def __init__(self):
                super().__init__(method=Player.move_west, name='Move west', hotkeys=['w', 'west'])


class ViewInventory(Action):
        """Prints the player's inventory"""
        def __init__(self):
                super().__init__(method=Player.print_inventory, name='View inventory', hotkeys=['i', 'inventory'])


class Attack(Action):
        def __init__(self, enemy):
                super().__init__(method=Player.attack, name="Attack", hotkeys=['a', 'attack'], enemy=enemy)


class Flee(Action):
        def __init__(self, tile):
                super().__init__(method=Player.flee, name="Flee", hotkeys=['f', 'flee like a lil bitch'], tile=tile)



