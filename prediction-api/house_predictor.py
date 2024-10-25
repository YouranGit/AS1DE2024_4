import joblib
from flask import jsonify
import json
import pandas as pd
from io import StringIO
from google.cloud import storage
import os
import json
class HousePredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, prediction_input):
        if self.model is None:
            # Load the .pkl model using pickle (for scikit-learn model)
            # with open("random_forest_model.pkl", "rb") as f:
            #     self.model = pickle.load(f)
            project_id = os.environ.get('PROJECT_ID', 'Specified environment variable is not set.')
            model_repo = os.environ.get('MODEL_REPO', 'Specified environment variable is not set.')
            client = storage.Client(project=project_id)
            bucket = client.bucket(model_repo)
            blob = bucket.blob("model.pkl")
            blob.download_to_filename('random_forest_model.pkl')
            self.model = joblib.load("random_forest_model.pkl")

        if isinstance(prediction_input, dict):
            prediction_input = [prediction_input]
        
        # Prepare the data by converting the JSON input into a pandas DataFrame
        df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')
        # Make predictions using the scikit-learn model
        y_pred = self.model.predict(df)
        print(y_pred)
        # Return the prediction result as a JSON response
        #return jsonify({'result': str(y_pred[0])}), 200
        return jsonify({'result': str(y_pred[0])}), 200

prediction_inputt = [ 
        {
                        "Median_Income": float(1),
                        "Median_Age": float(1),
                        "Tot_Rooms": float(1),
                        "Tot_Bedrooms": float(1),
                        "Population": float(1),
                        "Households": float(1),
                        "Latitude": float(1),
                        "Longitude": float(1),
                        "Distance_to_coast": float(1),
                        "Distance_to_LA": float(1),
                        "Distance_to_SanDiego": float(1),
                        "Distance_to_SanJose": float(1),
                        "Distance_to_SanFrancisco": float(1)

                    }
]
#dp = HousePredictor()
#dp.predict_single_record(prediction_inputt)