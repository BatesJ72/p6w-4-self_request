from flask import Flask, jsonify, render_template
import os
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    with open(os.path.join("owid-covid-2020-11-19-usa.csv")) as file:
        dict_reader = csv.DictReader(file)
        return jsonify(list(dict_reader))

if __name__ == "__main__":
    app.run(debug = True)