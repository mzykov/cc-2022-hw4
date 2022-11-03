class Department:

    def __init__(self, name):
        self.name = name
        self.employee_count = 0

    def update_count(self, delta):
        self.employee_count += int(delta)
        return self.employee_count

    def __repr__(self):
        parts = [ self.name, str(self.employee_count) ]
        return ' / '.join(parts)
