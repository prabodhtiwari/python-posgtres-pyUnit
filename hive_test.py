import unittest
import json
import subprocess

def first_test():
    return subprocess.check_output(["hdfs", "dfs", "-ls", "/user/hadoop/hive/dev/gglcloud/edh/"])

def second_test():
    return subprocess.check_output(["hive", "-S", "-e", "show databases"])


def third_test():
    return subprocess.check_output(["hive","--database", "dev_gglcloud_edh", "-S", "-e", "show tables"])

def forth_test():
    return subprocess.check_output(["hive","--database", "dev_gglcloud_edh", "-S", "-e", "describe dim_store"])

class MyTestCase(unittest.TestCase):
    def test_hive_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '"Found 6 items\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:42 /user/hadoop/hive/dev/gglcloud/edh/bad_consumer_experiment_discovery_visitor\\ndrwxrwxr-x   - hadoop hadoop       4096 2018-05-30 14:14 /user/hadoop/hive/dev/gglcloud/edh/dim_store\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:41 /user/hadoop/hive/dev/gglcloud/edh/dim_time_date\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:43 /user/hadoop/hive/dev/gglcloud/edh/fct_consumer_experiment_discovery_visitor\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:43 /user/hadoop/hive/dev/gglcloud/edh/fct_discovery_visitor_store_day_experiment\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-30 14:16 /user/hadoop/hive/dev/gglcloud/edh/raw_consumer_experiment_discovery_visitor\\n"')

    def test_hive_second_setup(self):
        second = second_test()
        self.assertEqual(json.dumps(second), '"default\\ndev_gglcloud_edh\\n"')

    def test_hive_third_setup(self):
        third = third_test()
        self.assertEqual(json.dumps(third), '"bad_consumer_experiment_discovery_visitor\\ndim_store\\ndim_time_date\\nfct_consumer_experiment_discovery_visitor\\nfct_discovery_visitor_store_day_experiment\\nraw_consumer_experiment_discovery_visitor\\n"')

    def test_hive_forth_setup(self):
        forth = forth_test()
        self.assertEqual(json.dumps(forth), '"storeid             \\tint                 \\tstore Integer Id    \\ntla                 \\tstring              \\tThree Letter Acronym for the store\\nname                \\tstring              \\tStore name          \\nstatus              \\tstring              \\tStatus of the store- whether it is A-active, I-inactive or X-deleted\\nsalescurrencycode   \\tstring              \\t                    \\n"')


if __name__ == '__main__':
    unittest.main()
