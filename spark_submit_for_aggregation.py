from pyhive import hive
import unittest
import json
import subprocess

conn = hive.Connection(host="0.0.0.0", port=10000, username="")
cursor = conn.cursor()


def first_test():
    cursor.execute("use dev_gglcloud_edh")
    cursor.execute("select * from raw_consumer_experiment_discovery_visitor")
    result = cursor.fetchall()
    return result


def second_test():
    cursor.execute("use dev_gglcloud_edh")
    cursor.execute("select * from bad_consumer_experiment_discovery_visitor")
    result = cursor.fetchall()
    return result


def third_test():
    cursor.execute("use dev_gglcloud_edh")
    cursor.execute("select * from fct_discovery_visitor_store_day_experiment")
    result = cursor.fetchall()
    return result

def forth_test():
    cursor.execute("use dev_gglcloud_edh")
    cursor.execute("select * from fct_consumer_experiment_discovery_visitor")
    result = cursor.fetchall()
    return result

class MyTestCase(unittest.TestCase):
    def test_hive_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '')

    def test_hive_second_setup(self):
        second = second_test()
        self.assertEqual(json.dumps(second), '')

    def test_hive_third_setup(self):
        third = third_test()
        self.assertEqual(json.dumps(third), '')

    def test_hive_forth_setup(self):
        forth = forth_test()
        self.assertEqual(json.dumps(forth), '')


if __name__ == '__main__':
    unittest.main()
