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
    def test_showinterfaces(self):
        r1 = r1 = Router('Cisco', 'IOSv', 'R1')
        r1.add_inf('Gigabit 0/1')
        r1.add_inf('Gigabit 0/2')
        self.assertIn('Gigabit 0/1', r1.interfaces)
        self.assertIn('Gigabit 0/2', r1.interfaces)
        self.assertEqual(len(r1.interfaces), 2)
    def test_showinterfaces2(self):
        r2 = Router('Cisco', '3745', 'R2')
        r2.add_inf('Gigabit 0/1')
        r2.add_inf('Gigabit 0/2')
        r2.add_inf('Gigabit 0/3')
        self.assertIn('Gigabit 0/1', r2.interfaces)
        self.assertIn('Gigabit 0/2', r2.interfaces)
        self.assertIn('Gigabit 0/3', r2.interfaces)
        self.assertEqual(len(r2.interfaces), 3)
    def test_showinterfaces3(self):
        r3 = Router('Juniper', 'MX5', 'R3')
        r3.add_inf('Gigabit 0/1')
        self.assertIn('Gigabit 0/1', r3.interfaces)
        self.assertEqual(len(r3.interfaces), 1)
if __name__ == '__main__':
    unittest.main()