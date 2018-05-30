from pyhive import hive

conn = hive.Connection(host="localhost", port=10000, username="hive")
cursor = conn.cursor()
cursor.execute("show databases")
for result in cursor.fetchall():
  print(result)