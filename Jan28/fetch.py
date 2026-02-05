import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT playerID, count(*)
    FROM Batting
    WHERE yearID = 1976
    GROUP BY playerID
    HAVING count(*) = 2
    ORDER by count(*) desc
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records)
print(records_df)