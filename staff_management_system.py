import unittest

from department import Department
from employee   import Employee
from position   import Position

class StaffManagementSystem:

    def __init__(self):
        self.departments = dict()
        self.employees_by_id = dict()
        self.employees_by_email = dict()
        self.employees_by_phone = dict()

    def add_department(self, name):
        self.departments[name] = Department(name)
        return self.departments[name]

    def add_departments(self, names):
        for name in names:
            self.add_department(name)

    def department(self, name, boss=None, parent=None):
        if name in self.departments.keys():
            department = self.departments[name]
            if boss:
                department.assign_boss(boss)
            if parent:
                department.set_parent(parent)
            return department
        else:
            return None

    def add_employee(self, name, email='', phone=''):
        return Employee(name, email=email, phone=phone);

    def create_company(self, name):
        return self.add_department(name)

    def assign_president(self, company, name):
        self.president = self.add_employee(name)
        position = self.add_position('President', company)
        self.employ(self.president, position)
        return self.president

    def add_position(self, name, department):
        position = Position(name, department)
        department.positions[name] = position
        return position

    def add_positions(self, names, department):
        for name in names:
            self.add_position(name, department)

    def employ(self, employee, position, boss=None):
        if position.is_vacant == False:
            raise ValueError
        self.close_position(employee, position)
        if boss == None:
            boss = position.department.boss
        if boss:
            self.assign_boss(employee, boss)
        self.employees_by_id[employee.id] = employee
        if employee.email:
            self.employees_by_email[employee.email] = employee
        if employee.phone:
            self.employees_by_phone[employee.phone] = employee
        return employee

    def retire(self, employee):
        del self.employees_by_id[employee.id]
        del self.employees_by_email[employee.email]
        del self.employees_by_phone[employee.phone]
        employee.boss.remove_subordinates(employee)
        employee.position.department.update_employee_count(-1)
        employee.position.vacant()
        return employee

    def close_position(self, employee, position):
        position.close()
        employee.position = position
        position.department.update_employee_count(1)

    def assign_boss(self, employee, boss):
        employee.boss = boss
        boss.update_subordinates(employee)

    def change_salary(self, employee, delta):
        employee.salary += delta
        return employee.salary

    def change_position(self, employee, new_position, salary_delta=0):
        self.retire(employee)
        self.employ(employee, new_position)
        if salary_delta != 0:
            self.change_salary(employee, salary_delta)

    def search_by_id(self, id):
        if id in self.employees_by_id.keys():
            return self.employees_by_id[id]
        else:
            return None

    def search_by_id(self, id):
        if id in self.employees_by_id.keys():
            return self.employees_by_id[id]
        else:
            return None

    def search_by_email(self, email):
        if email in self.employees_by_email.keys():
            return self.employees_by_email[email]
        else:
            return None

    def search_by_phone(self, phone):
        if phone in self.employees_by_phone.keys():
            return self.employees_by_phone[phone]
        else:
            return None

    def vacancies(self):
        res = []
        for name in self.departments.keys():
            positions = self.department(name).positions
            for pos in positions.keys():
                position = positions[pos]
                if position.is_vacant:
                    res.append(str(position))
        return res

    def print_company_tree(self):
        pass
