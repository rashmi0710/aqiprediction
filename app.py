from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle



application = Flask(__name__)
app = application

model = pickle.load(open('C:\\Users\\dongr\\OneDrive\\Desktop\\air_quality_predi\\linear.pkl', 'rb'))

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict_aqi():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            # Get the input data from the form
            data = request.form.to_dict()

            # Convert the input data to a numpy array for prediction
            input_data = np.array([
                [
                    float(data['nh3']),
                    float(data['pm2_5']),
                    float(data['pm10']),
                    float(data['o3']),
                    float(data['no2']),
                    float(data['so2']),
                    float(data['co'])
                ]
            ])

            # Make the prediction
            prediction = model.predict(input_data)

            # Return the predicted AQI as a JSON response
            return jsonify({'aqi': prediction[0]})
        except Exception as e:
            # Return an error message as JSON response
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
