import subprocess
import json
import unittest

def first_test():
    return subprocess.check_output(["cat", "/home/hadoop/output.csv"])


print first_test()


def test_hive_first_setup(self):
        first = first_test()
        self.assertEqual(json.dumps(first), '"Found 6 items\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:42 /user/hadoop/hive/dev/gglcloud/edh/bad_consumer_experiment_discovery_visitor\\ndrwxrwxr-x   - hadoop hadoop       4096 2018-05-30 14:14 /user/hadoop/hive/dev/gglcloud/edh/dim_store\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:41 /user/hadoop/hive/dev/gglcloud/edh/dim_time_date\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:43 /user/hadoop/hive/dev/gglcloud/edh/fct_consumer_experiment_discovery_visitor\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-28 18:43 /user/hadoop/hive/dev/gglcloud/edh/fct_discovery_visitor_store_day_experiment\\ndrwxr-xr-x   - hadoop hadoop       4096 2018-05-30 14:16 /user/hadoop/hive/dev/gglcloud/edh/raw_consumer_experiment_discovery_visitor\\n"')

if __name__ == '__main__':
    unittest.main()
