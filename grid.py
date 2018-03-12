class Board(object):
    Y_AXIS = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
    X_AXIS = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

    def __init__(self):
        self._units = {}
        self._attacks = []
        self._coords = {}

    def place(self, symbol, coord):
        x, y = coord
        x, y = self.X_AXIS[x], self.Y_AXIS[y]
        self._units[(x, y)] = symbol
        self._coords[symbol] = (x, y)

    def get(self, coord):
        return self._units[coord]

    def set_attack(self, attacker, x_delta, y_delta):
        self._attacks.append((attacker, x_delta, y_delta))

    def execute_attacks(self):
        for attack in self._attacks:
            self.execute_attack(*attack)

    def execute_attack(self, attacker, x_delta, y_delta):
        x, y = self._coords[attacker]
        target_x = x + x_delta
        target_y = y + y_delta
        target = target_x, target_y
        victim = self._units[target]
        victim.damage(1)

class Unit(object):
    def __init__(self, hp):
        self._hp = hp

    def damage(self, value=1):
        self._hp -= value

    def get_hp(self):
        return self._hp

