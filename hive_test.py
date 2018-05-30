from pyhive import hive
import unittest
import json
import subprocess

conn = hive.Connection(host="0.0.0.0", port=10000, username="")
cursor = conn.cursor()


def t():
    return subprocess.check_output(["hdfs", "dfs", "-ls", "/user/hadoop/hive/dev/gglcloud/edh/"])

print "jere"
print t()

def first_test():
    cursor.execute("show databases")
    result = cursor.fetchall()
    return result


def second_test():
    cursor.execute("use dev_gglcloud_edh")
    cursor.execute("show tables")
    result = cursor.fetchall()
    return result

def third_test():
    cursor.execute("use dev_gglcloud_edh")
    cursor.execute("describe dim_store")
    result = cursor.fetchall()
    return result

class MyTestCase(unittest.TestCase):
    def test_hive_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '[["default"], ["dev_gglcloud_edh"]]')

    def test_hive_second_setup(self):
        second = second_test()
        self.assertEqual(json.dumps(second), '[["bad_consumer_experiment_discovery_visitor"], ["dim_store"], ["dim_time_date"], ["fct_consumer_experiment_discovery_visitor"], ["fct_discovery_visitor_store_day_experiment"], ["raw_consumer_experiment_discovery_visitor"]]')

    def test_hive_third_setup(self):
        third = third_test()
        self.assertEqual(json.dumps(third), '[["storeid", "int", "store Integer Id"], ["tla", "string", "Three Letter Acronym for the store"], ["name", "string", "Store name"], ["status", "string", "Status of the store- whether it is A-active, I-inactive or X-deleted"], ["salescurrencycode", "string", ""]]')

    def test_hive_forth_setup(self):
        forth = t()
        self.assertEqual(json.dumps(forth), '"Found 6 items\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:42 /user/hadoop/hive/dev/gglcloud/edh/bad_consumer_experiment_discovery_visitor\\ndrwxrwxr-x   - hadoop hadoop       4096 2018-05-30 14:14 /user/hadoop/hive/dev/gglcloud/edh/dim_store\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:41 /user/hadoop/hive/dev/gglcloud/edh/dim_time_date\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:43 /user/hadoop/hive/dev/gglcloud/edh/fct_consumer_experiment_discovery_visitor\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:43 /user/hadoop/hive/dev/gglcloud/edh/fct_discovery_visitor_store_day_experiment\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-30 14:16 /user/hadoop/hive/dev/gglcloud/edh/raw_consumer_experiment_discovery_visitor\\n"')


if __name__ == '__main__':
    unittest.main()
