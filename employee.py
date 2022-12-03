import logging
import uuid

class AcceptedNDA:

    def __get__(self, obj):
        logging.info('Asked about NDA accpetance')
        return obj.is_accepted

    def __set__(self, obj, value):
        if value:
            logging.info('Employee %r accepted NDA', obj.id)
            obj.is_accepted = True
        else:
            logging.warning('Employee %r did not accept NDA', obj.id)

class Employee:

    accepted_NDA = AcceptedNDA()

    def __init__(self, name, age, nda, email='', phone=''):
        self.id = uuid.uuid1()
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.accepted_NDA = nda
        self.boss = None
        self.position = None
        self.subordinates = dict()

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False

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
