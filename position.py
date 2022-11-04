class Position:

    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.is_vacant = True

    def vacant(self):
        self.is_vacant = True

    def close(self):
        self.is_vacant = False

    def __repr__(self):
        parts = [ self.name, str(self.department) ]
        return ' / '.join(parts)
