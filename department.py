from position import Position

class Department:
    __positions = None
    __employee_count = None

    def __init__(self, name, boss=None, parent=None):
        self._name = name
        self._parent = parent
        self._boss = boss
        self.__positions = dict()
        self.__employee_count = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, p):
        self._parent = p

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, b):
        self._boss = b

    @property
    def employee_count(self):
        return self.__employee_count

    def update_employee_count(self, delta):
        self.__employee_count += int(delta)

    def add_position(self, name):
        position = Position(name, self)
        self.__positions[name] = position
        return position

    def add_positions(self, names):
        for name in names:
            self.add_position(name)

    def position(self, name):
        if name in self.__positions.keys():
            return self.__positions[name]
        else:
            return None

    def vacant_positions(self):
        return sorted(filter(lambda p: p.is_vacant, self.__positions.values()), key=lambda x: x.name)

    def __repr__(self, short=False):
        parts = [ self.name ]
        if short == False:
            parts.append(str(self.employee_count))
        return ' / '.join(parts)
