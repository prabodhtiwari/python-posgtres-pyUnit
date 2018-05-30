import db_client

def test():
    conn = db_client.connect()
    cur = conn.cursor()

    cur.execute("select * from dim_store")
    rows = cur.fetchall()
    res = ""
    for row in rows:
        res = row

    conn.close()
    return res

print test()