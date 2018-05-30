from pyhive import hive
import unittest
import json

conn = hive.Connection(host="0.0.0.0", port=10000, username="")
cursor = conn.cursor()

def first_test():
    cursor.execute("show databases")
    print cursor.description
    for result in cursor.fetchall():
        print(json.dumps(result))
    return result


def second_test():
    cursor.execute("use dev_gglcloud_edh")
    cursor.execute("show tables")
    print cursor.description
    result = cursor.fetchall()
    return result

class MyTestCase(unittest.TestCase):
    def test_hive_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '["dev_gglcloud_edh"]')

    def test_hive_second_setup(self):
        second = second_test()
        self.assertEqual(json.dumps(second), '[["bad_consumer_experiment_discovery_visitor"], ["dim_store"], ["dim_time_date"], ["fct_consumer_experiment_discovery_visitor"], ["fct_discovery_visitor_store_day_experiment"], ["raw_consumer_experiment_discovery_visitor"]]')

if __name__ == '__main__':
    unittest.main()
