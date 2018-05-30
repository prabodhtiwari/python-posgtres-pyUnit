import unittest
import  fetch

import db_client

def test():
    conn = db_client.connect()
    cur = conn.cursor()

    cur.execute("select * from dim_store")
    rows = cur.fetchall()
    conn.close()
    return rows

class MyTestCase(unittest.TestCase):
    def test_postgres_setup(self):
        greeter = fetch.test()
        self.assertEqual(greeter, [(1, 'one', 'Test Store One', 'A', 'USD'), (2, 'two', 'Test Store Two', 'A', None)])

if __name__ == '__main__':
    unittest.main()