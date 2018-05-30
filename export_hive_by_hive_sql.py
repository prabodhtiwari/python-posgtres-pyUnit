import subprocess
import json
import unittest
import os

def first_test():
    return subprocess.check_output(["hive", "-S", "-f", os.environ["EDHDIST"]+"/scripts/hql/dim_store_extract.sql"], env = d)

print first_test()

class MyTestCase(unittest.TestCase):
    def test_pig_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '"1\\tone\\tTest Store One\\tA\\tUSD\\n2\\ttwo\\tTest Store Two\\tA\\tNULL\\n"')

if __name__ == '__main__':
    unittest.main()
