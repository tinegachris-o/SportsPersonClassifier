from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # handles CORS for all routes automatically

@app.route("/classify_image", methods=["GET", "POST"])  # add POST
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server loading saved model into memory")
    util.load_saved_artifacts()
    app.run(host="0.0.0.0",port=7860)