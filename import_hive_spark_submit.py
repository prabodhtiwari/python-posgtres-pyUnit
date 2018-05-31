import unittest
import json
import subprocess

def first_test():
    return subprocess.check_output(["hive","--database", "dev_gglcloud_edh", "-S", "-e", "select * from dim_store"])

class MyTestCase(unittest.TestCase):
    def test_hive_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '"1\\tone\\tTest Store One\\tA\\tUSD\\n2\\ttwo\\tTest Store Two\\tA\\tNULL\\n"')


if __name__ == '__main__':
    unittest.main()
