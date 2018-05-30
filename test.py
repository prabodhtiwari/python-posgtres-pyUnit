import unittest
import  fetch

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = fetch.test()
        self.assertEqual(greeter, [(1, 'one', 'Test Store One', 'A', 'USD'), (2, 'two', 'Test Store Two', 'A', None)])

if __name__ == '__main__':
    unittest.main()