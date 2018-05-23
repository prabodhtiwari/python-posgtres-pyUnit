import unittest
import  fetch

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = fetch.test()
        self.assertEqual(greeter, 'Hello world!')

if __name__ == '__main__':
    unittest.main()