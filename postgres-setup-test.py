import unittest
import db_client
import datetime

def first_test():
    conn = db_client.connect()
    cur = conn.cursor()

    cur.execute("select * from dim_store")
    rows = cur.fetchall()
    conn.close()
    return rows


def second_test():
    conn = db_client.connect()
    cur = conn.cursor()

    cur.execute("select * from dim_time_date")
    rows = cur.fetchall()
    conn.close()
    return rows


class MyTestCase(unittest.TestCase):
    def test_postgres_setup(self):
        first = first_test()
        second = second_test()
        self.assertEqual(first, [(1, 'one', 'Test Store One',
                                  'A', 'USD'), (2, 'two', 'Test Store Two', 'A', None)])
        self.assertEqual(second, [(1, datetime.date(2018, 1, 1), 2018, 1, 1, 1), (2, datetime.date(2018, 1, 2), 2018, 1, 2, 2), (3, datetime.date(2018, 1, 3), 2018, 1, 3, 3), (4, datetime.date(
            2018, 1, 4), 2018, 1, 4, 4), (5, datetime.date(2018, 1, 5), 2018, 1, 5, 5), (6, datetime.date(2018, 1, 6), 2018, 1, 6, 6), (7, datetime.date(2018, 1, 7), 2018, 1, 7, 7)])


if __name__ == '__main__':
    unittest.main()
