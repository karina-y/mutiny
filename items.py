# -*- coding: utf-8 -*-

#superclass
class Item():
	"""the base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


#notsosuperclasses
class Gold(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Gold",
				 description="dolla dolla billz with {} stamped on the front.".format(str(self.amt)),
				 value=self.amt)


#WEAPONS
class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


#one rare ass kind of weapon
#class TheRock(Weapon):
#	def __init__(self):
#		super().__init__(name="'Rock, The'",
#				description="Do you smell what The Rock is cookin'? If you smeeellllll what The Rock is cookin', The Rock will bludgeon your enemy to death!",
#				value=100,
#				damage=50)


class Dagger(Weapon):
	def __init__(self):
		super().__init__(name="Dagger",
				description="A small dagger with some rust. It's no Rock but it's cool.... I guess...",
				value=0,
				damage=5)


class LegLamp(Weapon):
        def __init__(self):
                super().__init__(name="Leg Lamp",
                                description="The leg lamp from A Christmas Story, does pretty much nothing, maybe just annoys your enemies a bit",
                                value=0,
                                damage=1)


class FatBastard(Weapon):
        def __init__(self):
                super().__init__(name="Fat Bastard",
                                description="A large human who eats your enemies in one bite.. GET IN MAH BELLEH!!",
                                value=100,
                                damage=100)


class CellPhone(Weapon):
        def __init__(self):
                super().__init__(name="Cell Phone",
                                description="Snap a quick selfie before you die in some gruesome fashion or take a chance and throw your phone at the enemy",
                                value=2,
                                damage=5)


class RocketLauncher(Weapon):
        def __init__(self):
                super().__init__(name="Rocket Launcher",
                                description="Holy fucking shit it's a rocket launcher!!!! lol too bad there's no ammo to go with it ¯\_(ツ)_/¯",
                                value=75,
                                damage=2)
