from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('Linear_Regression_Model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])

        features = np.array([[area, bedrooms, bathrooms]])
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction=f"Estimated House Price: ${prediction:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)