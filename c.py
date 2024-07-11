from flask import Flask, render_template, request

import pickle

app = Flask(__name__)
model= pickle.load(open('model.sav','rb'))

@app.route('/')
def home():
    result =''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST' , 'GET'])
def predict():
        
        features_input = request.form['features']
    
        features = [float(x) for x in features_input.split(',')]
    
        prediction = model.predict([features])[0]

        if prediction == 0:
             
           result = 'Normal'

        else:
        
           result = 'Fraud'

        return render_template('index.html', **locals())

if __name__ ==  '__main__':
    app.run(debug=True)