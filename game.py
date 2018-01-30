import world
from player import Player
import random

def play():
	world.load_tiles()
	player = Player()
	#These lines load the starting room and display the text
	room = world.tile_exists(player.location_x, player.location_y)
	if room is None:
		room = world.tile_exists(2,0)
	print(room.intro_text())
	while player.is_alive() and not player.victory:
		#loop that shit
		room = world.tile_exists(player.location_x, player.location_y)
		room.modify_player(player)
		#check again since the room could've changed the player's state
		if player.is_alive() and not player.victory:
			#commented this shit out, prints the actions, we want them to guess
			#print("Choose an action:\n")
			available_actions = room.available_actions()
			#for action in available_actions:
			#	print(action)
			action_input = input('Action: ')
			action_found = False
			#print(available_actions)
			for action in available_actions:
				#print('hey', action)
				for hotkey in action.hotkeys:
					#print(action_input, action.hotkey)
					if action_input == hotkey:
						action_found = True
						player.do_action(action, **action.kwargs)
						break

			if not action_found:
				no_action_found = ["\nYOU CAN'T DO THAT\n", "ARGGHH The ocean be a dark place, if ye go that we ye'll fall to yer death\n", "\nOUCH bumped into a wall, ye should stop drinkin so much rum!\n"]
				print(random.choice(no_action_found))
				#print("\nYOU CAN'T DO THAT\n")


if __name__ == "__main__":
	play()
