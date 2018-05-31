from pyhive import hive
import unittest
import json
import subprocess

conn = hive.Connection(host="0.0.0.0", port=10000, username="")
cursor = conn.cursor()


def first_test():
    return subprocess.check_output(["hive","--database", "dev_gglcloud_edh", "-S", "-e", "select * from raw_consumer_experiment_discovery_visitor"])

def second_test():
    return subprocess.check_output(["hive","--database", "dev_gglcloud_edh", "-S", "-e", "select * from bad_consumer_experiment_discovery_visitor"])

def third_test():
    return subprocess.check_output(["hive","--database", "dev_gglcloud_edh", "-S", "-e", "select * from fct_discovery_visitor_store_day_experiment"])

def forth_test():
    return subprocess.check_output(["hive","--database", "dev_gglcloud_edh", "-S", "-e", "select * from fct_consumer_experiment_discovery_visitor"])

class MyTestCase(unittest.TestCase):
    def test_hive_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '[]')

    def test_hive_second_setup(self):
        second = second_test()
        self.assertEqual(json.dumps(second), '[]')

    def test_hive_third_setup(self):
        third = third_test()
        self.assertEqual(json.dumps(third), '[]')

    def test_hive_forth_setup(self):
        forth = forth_test()
        self.assertEqual(json.dumps(forth), '[]')


if __name__ == '__main__':
    unittest.main()
