import items, enemies, actions, world

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def adjacent_moves(self):
	        """Returns all move actions for adjacent tiles."""
	        moves = []
	        if world.tile_exists(self.x + 1, self.y):
	                moves.append(actions.MoveEast())
	        if world.tile_exists(self.x - 1, self.y):
	                moves.append(actions.MoveWest())
	        if world.tile_exists(self.x, self.y - 1):
	                moves.append(actions.MoveNorth())
	        if world.tile_exists(self.x, self.y + 1):
	                moves.append(actions.MoveSouth())
	        return moves

	def available_actions(self):
	        """Returns all of the available actions in this room."""
	        moves = self.adjacent_moves()
	        moves.append(actions.ViewInventory())
	        return moves

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, player):
		raise NotImplementedError()


class StartingRoom(MapTile):
	def intro_text(self):
		return """



                                                                   `
                                          ^''      ''-                 ` ''
                                                                   ,╓╓, ^^
                                                         ,,╓▄╗▄▓▓▄ç,╙▀▀█▀▄
                                                 ,▄▄▓█▓█▄▄Φ▀▀▀╙`  `''''''ⁿ   ╘
                                   ,▄▄▓▓▓▓▓▓██▌ ▀▀▀▀╙``
      ,                 ▄▄▄█▄▄██████▀╙└=-                   -     ╘    ▄⌐  '
      ╟      ╓▄▄▓Φ▓██▀▀▀▀▀▀▀▀╙''└        ^`                   ^        ▄█M,█
      ''    ╓██^                                          ║    ⌐µ     J█▌ ''█▌
            █                         ,▄,  ║╗   ▄        ║▌   ╝█▄    ║█   ██
            █    ,     ▄   `  ,   ,▄█▌▀''`   █∩  █▄       ▐█     ▀█V, ██   ▐█▌
            █         ╓█       ,═▀╙ ██      ▓█  ▐██▄▄     █       ╙███▌    ██
            ║         ██       ╙█⌐  ▐█L     ▐█▄  █▄`▀█▄▄  █∩        ⁿ█     ██▌
     ╔         █▄    ▐██▌ ╓▓∩   ╙█   ██      ║█  ╙█   ▀██└║▌        µ▌     ╙██
     ╙       .▄▄█    ██║║▌ ▀█    ▀█  ▀█       ▀¬  ▀█⌐  '▀███        █▌      ▀█▌
               ▀█▄▄ ,█▌ ██▄ █▌   ║██ ▐█▌           ▀▌     ██▌       ▐        ██
                ╙█└▀██  ╙█▌ ''▀█p,▌█   ▀'', .   ╙w     \,    ╙█               L▐█
              └  ▐▌      ╙█⌐   ╙▀█▀''     `   \    w         .         ~     ║ █▄
               ▌  █∩      ▀█            .«                                    ║█⌐
      ╘        ▓  ''█       ▌▌           `                     .  - ``     H   ██⌐
              ▐█   █▌             ^`        -                .≈══ⁿ^''[ .   L  ╫██^
              ▐█╒   █⌐\ ╓                                   <≡ª▀▀▀▀▀└ ,▄▄▄▄▄▓█▀
               █╙¥   ''   ,-          ,       ,,▄▄▄▄▄▄▄▄███████▓▓▀▀▀▀▀▀▀▀▀▀╙╙
               █▄  ],              ,▄▄▄▓████████████▀▀╙└        ^^
               ▐█▄ ,,     ,,╓╓▄▄███▀▀▀▀▀▀▀▀▀╙└└
                ╙████████▀▀▀▀╙└





       		You've just woken up in the hull of the Rogue Keel.
		The evil Kraken is somewhere on the ship hunting your crew.
		Find all the members of your crew before the Kraken eats them.
		"""

	def modify_player(self, player):
		#room has no action on player
		pass


class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)

	def add_loot(self, player):
		player.inventory.append(self.item)

	def modify_player(self, player):
		self.add_loot(player)


class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)

	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			if self.enemy.damage >= the_player.hp:
				print("lol u dead")
			elif self.enemy.damage < 50:
				print("{} does {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, the_player.hp))
			else:
				print("{} does {} damage. You have {} HP remaining. lol u got fuuuuuucked up.".format(self.enemy.name, self.enemy.damage, the_player.hp))

	def available_actions(self):
		if self.enemy.is_alive():
			return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
		else:
			return self.adjacent_moves()


#plain rooms
class EmptyPath(MapTile):
	def intro_text(self):
		return """
		Another unremarkable part of the cave. Your loneliness continues to glow like a little glowworm right in your belly
		"""

	def modify_player(self, player):
		#Room has no action on player
		pass


#enemy rooms
class TheRocksEvilTwinRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.TheRocksEvilTwin())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			You hear a whisper '....smell what ... the .......' from behind a boulder
			You move a little closer and hear some more whispers 'do you .... is cookin ...'
			You inch just a bit closer when suddenly a man resembling The Rock jumps out
			'DO YOU SMELL WHAT THE ROCK IS COOKIN', CUZ THE ROCK'S EVIL TWIN SMELLS WHAT THE ROCK IS COOOOKKIINNNNNNN'
			"""
		else:
			return """
			The corpse of The Rock's Evil Twin rots on the ground ....gross
			"""


class TheBigGiantHeadRoom(EnemyRoom):
        def __init__(self, x, y):
                super().__init__(x, y, enemies.TheBigGiantHead())

        def intro_text(self):
                if self.enemy.is_alive():
                        return """
                        Incoming message from The Big Giant Head
			You are about to get fucked up
                        """
                else:
                        return """
                        The corpse of The Big Giant Head rots on the ground ....gross
                        """


class TheBossRoom(EnemyRoom):
        def __init__(self, x, y):
                super().__init__(x, y, enemies.TheBoss())

        def intro_text(self):
                if self.enemy.is_alive():
                        return """
                        You are now facing the big boss, you know, the final enemy at the very end of a game that's like super hard to kill
                        """
                else:
                        return """
                        The corpse of The Big Boss rots on the ground ....gross
                        """


class SallyRoom(EnemyRoom):
        def __init__(self, x, y):
                super().__init__(x, y, enemies.Sally())

        def intro_text(self):
                if self.enemy.is_alive():
                        return """
			Sally is an angry amazon woman
			Sally was just chillin here selling her seashells by the seashore and you had to come up and disturb her
			Sally is ready to attack
                        """
                else:
                        return """
                        The corpse of Sally rots on the ground ....gross
                        """


class ScallywagRoom(EnemyRoom):
        def __init__(self, x, y):
                super().__init__(x, y, enemies.Scallywag())

        def intro_text(self):
                if self.enemy.is_alive():
                        return """
	Avast! Ye who cross Sammy the Scallywag's path may never return!
	I am loyal to the Kraken and will bring you in dead or alive! ARRGGHHH!!!
                        """
                else:
                        return """
	The corpse of Sammy the Scallywag rots on the ground ....gross
                        """



#loot rooms
class FindDaggerRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.Dagger())

	def intro_text(self):
		return """
		You notice something shiny in the corner.
		It's a dagger! You pick it up.
		As you yield the dagger you feel the power of a thousand suns surging through you
		every drop of blood running through your veins is blessed with the ichor of the gods
		jk it's just a rusty old dagger
		"""


class FindGoldRoom(LootRoom):
        def __init__(self, x, y):
                super().__init__(x, y, items.Gold(10))

        def intro_text(self):
                return """
                YOU'VE STRUCK GOLD! HUZZAAAHHHH!!!!
                """


class FindTheRockRoom(LootRoom):
        def __init__(self, x, y):
                super().__init__(x, y, items.TheRock())

        def intro_text(self):
                return """
                You look to the corner and notice an odd shadow
		is it a boulder? ...a shivering boulder? a huddled creature? no... no, it's THE ROCK
		that's right, THE Rock
		he's been looking for a home and it looks like he's found one, congratulations!
                """


class FindLegLampRoom(LootRoom):
        def __init__(self, x, y):
                super().__init__(x, y, items.LegLamp())

        def intro_text(self):
                return """
                what's that lit up in the center of the room? why it's a leg lamp! and a sexy one at that ; )
                """


class FindCellPhoneRoom(LootRoom):
        def __init__(self, x, y):
                super().__init__(x, y, items.CellPhone())

        def intro_text(self):
                return """
                you've found a cell phone! you could call for help but unfortunately it's just one of those stupid display phones from Best Buy
                """


class FindRocketLauncherRoom(LootRoom):
        def __init__(self, x, y):
                super().__init__(x, y, items.RocketLauncher())

        def intro_text(self):
                return """
                A MOTHERFUCKING ROCKET LAUNCHER
                """


class LeaveCaveRoom(MapTile):
	def intro_text(self):
		return """
		YASSSSSS BITCH U HAVE ESCAPED THE CAVE OF TERRORS U GO GLEN COCO!!!
		"""

	def modify_player(self, player):
		player.victory = True
