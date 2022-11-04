import unittest
from position import Position

class TestPosition(unittest.TestCase):

    def test_vacancy(self):
        position = Position('Team Lead', 'IT')
        self.assertTrue(position.is_vacant)
        position.close()
        self.assertFalse(position.is_vacant)
        position.vacant()
        self.assertTrue(position.is_vacant)

    def test_representation(self):
        position = Position('Team Lead', 'IT')
        self.assertEqual(str(position), 'Team Lead / IT')

if __name__ == '__main__':
    unittest.main()
