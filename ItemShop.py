# Class containing purchasable items


class Item:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage


class ItemShop:
    def __init__(self):
        self.items = [Item('Dagger', 10, 5), Item('Long Sword', 20, 10)]

    def sell(self, player, item):
        if player.gold >= item.cost:
            player.item = item
            print('You have acquired ' + item.name)
        else:
            print("You don't have enough gold")
