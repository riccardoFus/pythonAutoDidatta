import unittest
from city_functions import define_city

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = define_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')
    
    def test_city_country_population(self):
        formatted_city = define_city('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - 5000000')

if __name__ == '__main__':
    unittest.main()