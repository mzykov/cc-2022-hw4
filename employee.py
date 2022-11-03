class Employee:

    def __init__(self, name, email='', phone=''):
        self.name  = name
        self.email = email
        self.phone = phone

    def update_email(self, email):
        if email:
            self.email = email
        return self.email

    def update_phone(self, phone):
        if phone:
            self.phone = phone
        return self.phone
