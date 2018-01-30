class Enemy:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def is_alive(self):
		return self.hp > 0


class TheBigGiantHead(Enemy):
	def __init__(self):
		super().__init__(name="The Big Giant Head", hp=10, damage=2)


class Bowser(Enemy):
        def __init__(self):
                super().__init__(name="Bower", hp=14, damage=4)


class Sally(Enemy):
        def __init__(self):
                super().__init__(name="Sally gon' fuck u up", hp=100, damage=20)


class TheRocksEvilTwin(Enemy):
        def __init__(self):
                super().__init__(name="The Rock's Evil Twin MUAHAHAHA", hp=85, damage=15)


class TheBoss(Enemy):
        def __init__(self):
                super().__init__(name="The Boss", hp=900, damage=2)
