from pyhive import hive
import unittest
import json
import subprocess

conn = hive.Connection(host="0.0.0.0", port=10000, username="")
cursor = conn.cursor()


def first_test():
    cursor.execute("select * from dev_gglcloud_edh.dim_store")
    result = cursor.fetchall()
    return result

print json.dumps(first_test())


class MyTestCase(unittest.TestCase):
    def test_hive_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '')


if __name__ == '__main__':
    unittest.main()
