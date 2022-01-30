from flask import Flask, jsonify, request
import csv

with open('new_stars.csv', newline="") as f:
  reader = csv.reader(f)
  data = list(reader)

app = Flask(__name__)
 
@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200
 
@app.route("/stars")
def stars():
    name = request.args.get("Star_name")             #Args is the argument which we are passing in the bracket
       
    star = []

    for i in data:
        if i[1] == name:
            star.append(i)

    return jsonify({
        "data": star,
        "message": "success"
    }), 200
 
if __name__ == "__main__":
    app.run()
