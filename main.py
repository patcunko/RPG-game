encounter = {(1, 0): 0, (1, 0): 0, (1, 1): 3, (1, 2): 0, (1, 3): 2, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (2, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0,
             (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0, (1, 0): 0}
over = False
valid = False


class Player:
    health = 10
    damage = 2
    location = [0, 0]
    previous_location = [0, 0]
    gold = 0
    weapon = ''
    if weapon == 'Dagger':
        damage = 5


class Shop:
    item_1 = 'Dagger'
    item_2 = 'Long Sword'
    item_1_cost = 10
    item_2_cost = 20
    item_1_damage = 5
    item_2_damage = 10


def new_weapon():
    valid_selection = False

    while not valid_selection:
        selection = input('Select one of the following: , '
                          'Dagger: 10 gold, 5 Damage , '
                          'Long Sword: 20 gold 10 Damage , '
                          'or B for back')

        if selection == Shop.item_1 and Player.gold >= Shop.item_1_cost:
            Player.weapon = Shop.item_1
            Player.gold -= Shop.item_1_cost
            Player.damage = Shop.item_1_damage
            valid_selection = True
            print('You have acquired ' + Shop.item_1)
            encounter[Player.location[0], Player.location[1]] = 0
        elif selection == Shop.item_1 and Player.gold < Shop.item_1_cost:
            print("You don't have enough gold")

        if selection == Shop.item_2 and Player.gold >= Shop.item_2_cost:
            Player.weapon = Shop.item_2
            Player.gold -= Shop.item_2_cost
            Player.damage = Shop.item_2_damage
            valid_selection = True
            print('You have acquired ' + Shop.item_2)
            encounter[Player.location[0], Player.location[1]] = 0
        elif selection == Shop.item_2 and Player.gold < Shop.item_2_cost:
            print("You don't have enough gold")

        if selection == 'B':
            Player.location[0] = Player.previous_location[0]
            Player.location[1] = Player.previous_location[1]
            valid_selection = True


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


def play():
    global valid_choice
    walk(direction)
    valid_choice = False


valid_choice = False

while not over or not valid:
    direction = input('F for Forward, R for Right, L for Left or B for Back?')
    play()

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
