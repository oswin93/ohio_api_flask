from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_annual_data(api_well_number):

    conn = sqlite3.connect('well_production.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT OIL, GAS, BRINE FROM annual_production WHERE API_WELL_NUMBER = ?", (api_well_number,))
    row = cursor.fetchone()

    conn.close()

    if row:
         return {
            "OIL": row[0],
            "GAS": row[1],
            "BRINE": row[2]
        }
    return None


@app.route('/report', methods=['GET'])
def api_get_annual_data():
    well_number = request.args.get('api_well_number')
    if not well_number:
        return jsonify({"error": "Please provide a 'api_well_number' query parameter."}), 400
    try:
        data = get_annual_data(well_number)
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"error": "Data not found for the specified well."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080)

"""To get production data for a specific well, make a GET request to:"""
# http://127.0.0.1:8080/report?api_well_number=<API_WELL_NUMBER>
