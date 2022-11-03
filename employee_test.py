import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emploee = Employee('Empl name', email='old@email')
        self.assertEqual(emploee.email, 'old@email')
        emploee.update_email('new@email')
        self.assertEqual(emploee.email, 'new@email')

    def test_phone(self):
        emploee = Employee('Empl name', phone='+79667861234')
        self.assertEqual(emploee.phone, '+79667861234')
        emploee.update_phone('+79660987761')
        self.assertEqual(emploee.phone, '+79660987761')

if __name__ == '__main__':
    unittest.main()
