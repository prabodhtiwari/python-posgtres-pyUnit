import subprocess
import json
import unittest

def first_test():
    return subprocess.check_output(["cat", "/home/hadoop/output.csv"])

class MyTestCase(unittest.TestCase):
    def test_pig_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '"one,Test Store One,A,USD\\ntwo,Test Store Two,A,\\n"')

if __name__ == '__main__':
    unittest.main()
