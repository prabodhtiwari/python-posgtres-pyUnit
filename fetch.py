import db_client

def test():
    conn = db_client.connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users")
    rows = cur.fetchall()
    res = ""
    for row in rows:
        res = row[0]

    conn.close()
    return res

print test()