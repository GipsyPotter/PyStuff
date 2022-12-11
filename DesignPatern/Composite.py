#Rank tree
class Soldier:

    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end="")
        print(self.position)


class Sergant:
    def __init__(self, *args):

        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()


if __name__ == "__main__":
    topLevelMenu = Sergant("General")
    subMenuItem1 = Sergant("Sergant1")
    subMenuItem2 = Sergant("Sergant2")
    subMenuItem1_1 = Soldier("Soldier1_1")
    subMenuItem1_2 = Soldier("Soldier1_2")
    subMenuItem1_1 = Soldier("Soldier2_1")
    subMenuItem2_2 = Soldier("Soldier2_2")
    subMenuItem1.add(subMenuItem1_1)
    subMenuItem1.add(subMenuItem1_2)
    subMenuItem2.add(subMenuItem2_2)
    subMenuItem2.add(subMenuItem2_2)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()
