# All possible player locations
from ItemShop import ItemShop

encounter = {(1, 0): 0, (2, 0): 2, (1, 1): 1, (1, 2): 0, (1, 3): 2, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (0, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0}

over = False
valid = False


# Class containing players stats and equipment


class Player:
    item = None
    health = 10
    damage = 2
    location = [0, 0]
    previous_location = [0, 0]
    gold = 0
    weapon = ''
    if weapon == 'Dagger':
        damage = 5


Shop = ItemShop()


# Function that checks for valid response then checks players gold and gives them a response accordingly


def new_weapon():
    valid_selection = False

    while not valid_selection:
        selection = input('Select one of the following: , '
                          'Dagger: 10 gold, 5 Damage , '
                          'Long Sword: 20 gold 10 Damage , '
                          'or B for back')

        if selection == Shop.items[0].name:
            Shop.sell(Player, Shop.items[0])
            valid_selection = True
            encounter[Player.location[0], Player.location[1]] = 0

        if selection == Shop.items[1].name:
            Shop.sell(Player, Shop.items[1])
            valid_selection = True
            encounter[Player.location[0], Player.location[1]] = 0

        if selection == 'B':
            Player.location[0] = Player.previous_location[0]
            Player.location[1] = Player.previous_location[1]
            valid_selection = True


# Class for enemies and enemy stats containing a method for fighting when encountered by player


class Enemy:
    def __init__(self, name='', health=0, damage=0, enemy_location=None, worth=0):
        if enemy_location is None:
            enemy_location = [0, 0]
        self.name = name
        self.health = health
        self.damage = damage
        self.location = enemy_location
        self.worth = worth

    def fight(self, p_health, p_damage):
        global over
        global encounter

        while p_health > 0 and self.health > 0:
            p_health -= self.damage
            self.health -= p_damage

            if self.health <= 0:
                print('You defeated the ' + self.name + '! You have ' + str(p_health) + ' health remaining')
                encounter[self.location[0], self.location[1]] = 0
                Player.gold += self.worth

            if p_health <= 0:
                print('You died')
                over = True


Ogre = Enemy('Ogre', 5, 2, [1, 3], 10)


# Function for a player move


def walk(picked_direction):
    global valid

    if picked_direction == 'F':
        Player.previous_location[0] = Player.location[0]
        Player.previous_location[1] = Player.location[1]
        Player.location[1] += 1
        valid = True
    elif picked_direction == 'B':
        Player.previous_location[0] = Player.location[0]
        Player.previous_location[1] = Player.location[1]
        Player.location[1] -= 1
        valid = True
    elif picked_direction == 'R':
        Player.previous_location[0] = Player.location[0]
        Player.previous_location[1] = Player.location[1]
        Player.location[0] += 1
        valid = True
    elif picked_direction == 'L':
        Player.previous_location[0] = Player.location[0]
        Player.previous_location[1] = Player.location[1]
        Player.location[0] -= 1
        valid = True


# start of game function


def play():
    global valid_choice
    walk(direction)
    valid_choice = False


valid_choice = False

# Starts game and checks for valid responses then moves player accordingly
while not over or not valid:
    direction = input('F for Forward, R for Right, L for Left or B for Back?')
    play()

    # Conditionals for different events depending on player location
    if encounter[Player.location[0], Player.location[1]] == 2:
        while not valid_choice:
            choice = input('You encountered an Ogre, select A for Attack or R for Run')
            if choice == 'A':
                Ogre.fight(Player.health, Player.damage)
                valid_choice = True
            elif choice == 'R':
                Player.location[0] = Player.previous_location[0]
                Player.location[1] = Player.previous_location[1]
                valid_choice = True
                print('You ran away')

    if encounter[Player.location[0], Player.location[1]] == 3:
        while not valid_choice:
            choice = input('You encountered a merchant, would you like to buy (Y for yes, N for no)')
            if choice == 'Y':
                new_weapon()
                valid_choice = True
            elif choice == 'N':
                valid_choice = True

    if encounter[Player.location[0], Player.location[1]] == 1:
        Player.location[0] = Player.previous_location[0]
        Player.location[1] = Player.previous_location[1]
        print("There is a wall, pick another direction")
