from flask import Flask, request
from flask_cors import CORS
#import model  # This is your model inference module

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = data["text"].upper() # Call your model inference function
    return {"prediction": prediction}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)