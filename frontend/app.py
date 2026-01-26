from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/predict"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        data = {
            "CRIM": float(request.form["CRIM"]),
            "ZN": float(request.form["ZN"]),
            "INDUS": float(request.form["INDUS"]),
            "CHAS": int(request.form["CHAS"]),
            "NOX": float(request.form["NOX"]),
            "RM": float(request.form["RM"]),
            "AGE": float(request.form["AGE"]),
            "DIS": float(request.form["DIS"]),
            "RAD": int(request.form["RAD"]),
            "TAX": float(request.form["TAX"]),
            "PTRATIO": float(request.form["PTRATIO"]),
            "B": float(request.form["B"]),
            "LSTAT": float(request.form["LSTAT"])
        }

        response = requests.post(FASTAPI_URL, json=data)
        prediction = response.json()["predicted_price"]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
