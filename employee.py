import uuid

class Employee:

    def __init__(self, name, email='', phone=''):
        self.id = uuid.uuid1()
        self.name = name
        self.email = email
        self.phone = phone
        self.boss = None
        self.position = None
        self.subordinates = dict()

    def update_email(self, email):
        if email:
            self.email = email
        return self.email

    def update_phone(self, phone):
        if phone:
            self.phone = phone
        return self.phone

    def id(self):
        return self.id

    def update_subordinates(self, employee):
        self.subordinates[employee.id] = employee

    def remove_subordinates(self, employee):
        employee.boss = None
        del self.subordinates[employee.id]

    def __repr__(self):
        parts = [ self.name ]
        if self.email:
            parts.append(self.email)
        if self.phone:
            parts.append(self.phone)
        return ' / '.join(parts)
