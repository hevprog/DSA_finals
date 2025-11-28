from copy import deepcopy

class Hanoi_logic:

    def __init__(self, disks):

        self.disks = disks
        self.towers = [
            [],
            [],
            [],
            []
        ]

        for x in range(1,disks + 1):
            self.towers[0].append(x)

    def move_disk(self, from_tower, to_tower):
        #check no disk
        if not self.towers[from_tower]:
            return False
        
        disks = self.towers[from_tower][-1]
        #check invalid move
        if self.towers[to_tower] and self.towers[to_tower][-1] < disks:
            return False 

        self.towers[from_tower].pop()
        self.towers[to_tower].append(disks)
        return True

    def get_towers(self):
        return deepcopy(self.towers)


if __name__ == "__main__":
    h = Hanoi_logic(3)

    print(h.get_towers())
    print(h.move_disk(0,2))
    print(h.get_towers())
    print(h.move_disk(0,3))
    print(h.get_towers())
    print(h.move_disk(2,1))
    print(h.get_towers())
    print(h.move_disk(0,2))
    print(h.get_towers())