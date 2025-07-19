from flask import Flask, jsonify, request
from flask_cors import cross_origin
import joblib
from numpy import array

iris_classifier_file = "model/iris_classifier.sav"
iris_scaler_file = "model/iris_scaler.joblib"

app = Flask(__name__)

iris_classifier = joblib.load(iris_classifier_file)
iris_scaler = joblib.load(iris_scaler_file)

iris_targets = ["setosa", "versicolor", "virginica"]

@app.route("/", methods=["POST"])
@cross_origin()
def predict_iris():
    request_data = request.json
    if request_data:
        try:
            sepal_length = float(request_data.get("sepal_length"))
            sepal_width = float(request_data.get("sepal_width"))
            petal_length = float(request_data.get("petal_length"))
            petal_width = float(request_data.get("petal_width"))
        except:
            raise ValueError("Petal and Sepal data not propagated as expected")
        
        predict_data = array([[sepal_length, sepal_width, petal_length, petal_width]])
        predict_data = iris_scaler.transform(predict_data)

        target_name = iris_targets[iris_classifier.predict(predict_data).tolist()[0]-1]
        return jsonify({"target_name": target_name})
    else:
        raise ValueError("Petal and Sepal data expected as JSON body")
    
if __name__ == "__main__":
    app.run(debug=True)