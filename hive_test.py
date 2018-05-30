from pyhive import hive
import unittest
import json

conn = hive.Connection(host="0.0.0.0", port=10000, username="hive")
cursor = conn.cursor()

# def first_test():
cursor.execute("show databases")
for result in cursor.fetchall():
# print(json.dumps(result))
 print result

# print first_test()

# class MyTestCase(unittest.TestCase):
#     def test_hive_first_setup(self):
#         first = first_test()
#         self.assertEqual(first, (u'default',)
# (u'dev_gglcloud_edh',))


# if __name__ == '__main__':
#     unittest.main()
