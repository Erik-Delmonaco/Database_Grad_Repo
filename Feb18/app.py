import sqlite3
import gradio as gr
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    WITH top_hitters AS (SELECT nameFirst, nameLast, batting.playerID
    FROM people INNER JOIN Batting
    ON people.playerID = Batting.playerID
    WHERE teamID = 'PHI'
    GROUP BY Batting.playerID
    ORDER BY SUM(HR) desc
    LIMIT 10)

    SELECT CONCAT(nameFirst,' ',nameLast), playerID
    FROM top_hitters
    ORDER BY nameLast
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

def f(playerID):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT CAST(yearID AS text), HR
        FROM Batting
        WHERE teamID = 'PHI' AND playerID = ?
        ORDER BY yearID
    """
    cursor.execute(query,[playerID])
    records = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(records, columns = ["year","home runs"])
    return df




with gr.Blocks() as iface:
    name_box = gr.Dropdown(records,interactive = True)
    plot = gr.LinePlot(x = "year",y = "home runs")
    name_box.change(fn = f,inputs = [name_box],outputs = [plot])

iface.launch()