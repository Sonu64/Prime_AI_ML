class Player:
    # Class variables
    playerCount = 0
    def __init__(self, name, level):
        Player.playerCount += 1
        # Instance Variables
        self.name = name
        self.level = level
    
p1 = Player("Sonu", 10)
p2 = Player("Shanu", 5)
print(f"Total Players created till now are {Player.playerCount}")


