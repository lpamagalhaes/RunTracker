import gpxpy.gpx
import sqlite3
from flask import Flask, jsonify

app = Flask('Luis paulo')

conn = sqlite3.connect(':memory:', check_same_thread=False)


sql_create_points_table = """CREATE TABLE IF NOT EXISTS points (
                                    id integer PRIMARY KEY,
                                    latitude real NOT NULL,
                                    longitude real NOT NULL,
                                    elevation real NOT NULL
                                ); """

c = conn.cursor()
c.execute(sql_create_points_table)
conn.commit()

@app.route('/load', methods=['GET'])
def load_points():
    with open('Corrida_matinal.gpx') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                sql_insert_point = f'''INSERT INTO points(latitude,longitude,elevation) VALUES('{point.latitude}','{point.longitude}','{point.elevation}')'''
                c.execute(sql_insert_point)
                conn.commit()

    return '', 200


@app.route('/points', methods=['GET'])
def get_points():
    content = list()

    sql_query_tracks = 'select * from points'
    result = c.execute(sql_query_tracks)
    rows = result.fetchall()

    return jsonify(rows)



app.run(host='localhost', port=5000)
