from random import choice


class TinWoodman:
    wood_data = {'Young pine': {'blows': 1, 'oil': 10, 'income': 2},
                 'Spruce': {'blows': 2, 'oil': 7.5, 'income': 3},
                 'Cedar': {'blows': 3, 'oil': 6, 'income': 4},
                 'Oak': {'blows': 5, 'oil': 8, 'income': 10}}
    oil = [100, 0]
    overall_wood = 0
    wood_planks = 0
    tree_health = None
    cur_tree = None
    die = False
    main_script = "Choose an action:\n1 - tree search;\n2 - refill oil;\n3 - statistics;\n4 - come back home.\n"
    tree_script = "Choose an action:\n1 - cut down a tree;\n2 - refill oil;\n3 - statistics;\n4 - come back home.\n"

    def main_work(self):
        request = 1
        print('Lumberjack starts working in the forest')
        while request != 4 and not self.die:
            if self.cur_tree == None:
                print(self.main_script)
            else:
                print(self.tree_script)
            request = int(input('Answer:'))
            if self.cur_tree == None:
                if request == 1:
                    self.search_tree()
                elif request == 2:
                    self.fill_oil()
                elif request == 3:
                    self.stat()
            else:
                if request == 1:
                    self.cut_tree()
                elif request == 2:
                    self.fill_oil()
                elif request == 3:
                    self.stat()
        if self.die:
            print('Oh no! The oil is out!')
            print('The woodcutter is rusty, the game is over.')
            print()
            self.stat()
        else:
            self.end_work()

    def search_tree(self):
        self.cur_tree = choice(list(self.wood_data.keys()))
        self.tree_health = 0
        print('The woodcutter finds', self.cur_tree + '!')

    def cut_tree(self):
        self.tree_health += 1
        self.lower_oil()
        print('The woodcutter takes a hit on', self.cur_tree,
              '(' + str(self.tree_health) + '/' + str(self.wood_data[self.cur_tree]['blows']) + ')')
        print('Oil', '(' + str(self.oil[0]) + '/100)')
        if self.die:
            return
        if self.tree_health == self.wood_data[self.cur_tree]['blows']:
            self.overall_wood += self.wood_data[self.cur_tree]['income']
            self.wood_planks += 1
            print('The tree fell, the woodcutter gets', self.wood_data[self.cur_tree]['income'], 'boards.')
            self.cur_tree = None

    def lower_oil(self):
        self.oil[0] -= self.wood_data[self.cur_tree]['oil']
        if self.oil[0] < 0:
            self.die = True

    def fill_oil(self):
        print('The woodcutter takes the tube of oil')
        self.oil[1] += 100 - self.oil[0]
        self.oil[0] = 100
        print('Oil 100/100')

    def stat(self):
        print('Statistics:')
        print('Oil:', str(self.oil[0]) + '/100')
        print('All used oil:', self.oil[1])
        print('Boards:', self.overall_wood)
        print('Downed trees:', self.wood_planks)

    def end_work(self):
        print('After a hard day\' work, the woodcutter goes home')
        self.stat()


tw = TinWoodman()
tw.main_work()