import db_client

def test():
    conn = db_client.connect()
    cur = conn.cursor()

    cur.execute("select * from dim_time_date")
    rows = cur.fetchall()
    res = ""
    for row in rows:
        res = rows

    conn.close()
    return res

print test()