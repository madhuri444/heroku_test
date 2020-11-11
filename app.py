import numpy as np
import pickle
from trial_file import*
from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
model = pickle.load(open("pickle.pkl","rb"))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods = ['post'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    print(prediction)
    output = prediction[0]
    p = int(output)
    x = func()
    print(x[p])

    #dict1 = {0: 'Bream', 4: 'Roach', 6: 'Whitefish', 1: 'Parkki', 2: 'Perch', 3: 'Pike', 5: 'Smelt'}
    output1 = x[p]
    return render_template('index1.html', prediction_text='Fish Category is {}'.format(output1))



if __name__ == "__main__":
    app.run(debug=True)