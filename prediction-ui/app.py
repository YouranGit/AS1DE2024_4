# importing Flask and other modules
import os
import json
import logging
import requests
from flask import Flask, request, render_template, jsonify

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route("/checkprice", methods=["GET", "POST"])
def check_price():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        prediction_input = [
            {
                "Median_Income": float(request.form.get("feature_1")),
                "Median_Age": float(request.form.get("feature_2")),
                "Tot_Rooms": float(request.form.get("feature_3")),
                "Tot_Bedrooms": float(request.form.get("feature_4")),
                "Population": float(request.form.get("feature_5")),
                "Households": float(request.form.get("feature_6")),
                "Latitude": float(request.form.get("feature_7")),
                "Longitude": float(request.form.get("feature_8")),
                "Distance_to_coast": float(request.form.get("feature_9")),
                "Distance_to_LA": float(request.form.get("feature_10")),
                "Distance_to_SanDiego": float(request.form.get("feature_11")),
                "Distance_to_SanJose": float(request.form.get("feature_12")),
                "Distance_to_SanFrancisco": float(request.form.get("feature_13"))


            }
        ]

        logging.debug("Prediction input : %s", prediction_input)

        predictor_api_url = os.environ['PREDICTOR_API']
        #predictor_api_url = "http://localhost:5000/house_predictor"
        res = requests.post(predictor_api_url, json=json.loads(json.dumps(prediction_input)))

        prediction_value = res.json()['result']
        logging.info("Prediction Output : %s", prediction_value)
        return render_template("result.html",
                               prediction_variable=prediction_value)

    else:
        return jsonify(message="Method Not Allowed"), 405

# The code within this conditional block will only run the python file is executed as a script.
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5001)), host='0.0.0.0', debug=False)