import unittest
from employee import Employee

class TestEmployeeMethods(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('Riccardo', 'Fusiello', 4000)
    
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(9000, self.my_employee.salary)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(14000, self.my_employee.salary)

if __name__ == '__main__':
    unittest.main()