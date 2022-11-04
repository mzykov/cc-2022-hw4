class Department:

    def __init__(self, name, boss=None, parent=None):
        self.name = name
        self.employee_count = 0
        self.positions = dict()
        self.parent = parent
        self.boss = boss

    def update_employee_count(self, delta):
        self.employee_count += int(delta)
        return self.employee_count

    def add_position(self, name):
        position = Position(name, self)
        self.positions[name] = position

    def add_positions(self, names):
        for name in names:
            self.add_position(name)

    def position(self, name):
        if name in self.positions.keys():
            return self.positions[name]
        else:
            return None

    def assign_boss(self, boss):
        self.boss = boss

    def set_parent(self, parent):
        self.parent = parent

    def __repr__(self, short=False):
        parts = [ self.name ]
        if short == False:
            parts.append(str(self.employee_count))
        return ' / '.join(parts)
