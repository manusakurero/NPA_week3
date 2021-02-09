from Router import Router
import unittest

class TestRouter(unittest.TestCase):
    def test_addinf1(self):
        r1 = Router('Cisco', 'IOSv', 'R1')
        r1.add_inf('Gigabit 0/1')
        self.assertIn('Gigabit 0/1', r1.interfaces)
    def test_addinf2(self):
        r1 = Router('Cisco', 'IOSv', 'R1')
        r1.add_inf('Gigabit 0/2')
        self.assertIn('Gigabit 0/2', r1.interfaces)
    def test_addinf3(self):
        r2 = Router('Cisco', '3745', 'R2')
        r2.add_inf('Gigabit 0/2')
        self.assertIn('Gigabit 0/2', r2.interfaces)
    def test_addinf4(self):
        r2 = Router('Cisco', '3745', 'R2')
        r2.add_inf('Gigabit 0/2')
        self.assertIn('Gigabit 0/2', r2.interfaces)
    def test_addinf5(self):
        r2 = Router('Cisco', '3745', 'R2')
        r2.add_inf('Gigabit 0/3')
        self.assertIn('Gigabit 0/3', r2.interfaces)
if __name__ == '__main__':
    unittest.main()