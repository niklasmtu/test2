class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0

    def take_damage(self, damage):
        self.health = self.health - damage

    def add_score(self, points):
        self.score = self.score + points

    def show_status(self):
        print("Player:", self.name)
        print("Health:", self.health)
        print("Score:", self.score)


player1 = Player("Alex")

player1.show_status()

player1.take_damage(20)
player1.add_score(100)

player1.show_status()