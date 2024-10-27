# Ohio Production Data API

This is a Flask-based API that provides annual oil, gas, and brine production data for wells in Ohio based on their API Well Number.

* REST API to access annual production data.
* Built using Flask, with SQLite as the database.

### Prerequisites
* Python 3.7+

### Installation
* pip install -r requirements.txt

### Running the Application

Run the Flask app using:

python app.py

The app should now be accessible at http://localhost:8080.

## Usage

To get production data for a specific well, make a GET request to:

http://127.0.0.1:8080/report?api_well_number=<**api_well_number**>

### Expected response:

{
  "oil": 381,
  "gas": 108074,
  "brine": 939
}


## Folder Structure

* app.py - Main application file to run the Flask server.
* db_connection.py - Loading annual data to Sqlite database
* well_production.db - SQLite database containing production data.
* data_loading.py - data calculation and manipulation using Pandas
* request.py - For downloading the data from given url
* requirements.txt - List of dependencies.
* README.md - Project documentation.# ohio_api_flask
