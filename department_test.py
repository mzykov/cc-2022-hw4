import unittest
from department import Department

class TestDepartment(unittest.TestCase):

    def test_update_employee_count(self):
        department = Department('Python Developers')
        department.update_employee_count(17)
        self.assertEqual(department.employee_count, 17)
        department.update_employee_count(-3)
        self.assertEqual(department.employee_count, 14)

    def test_set_parent(self):
        it_dep = Department('IT')
        coders_dep = Department('Python Developers')
        coders_dep.parent = it_dep
        self.assertIsNone(it_dep.parent);
        self.assertEqual(coders_dep.parent, it_dep);

    def test_representation(self):
        department = Department('Python Developers')
        department.update_employee_count(17)
        self.assertEqual(str(department), 'Python Developers / 17')

if __name__ == '__main__':
    unittest.main()
