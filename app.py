import numpy as np
import flask
from flask import Flask , request, jsonify , render_template
import pickle

app = Flask(__name__)  # creation of flask app

lm_model = pickle.load(open('lm_model.pkl','rb'))  #'rb' stands for 'read bytes'

@app.route('/')
def home():   # this will be the homepage
    return render_template('index.html')   

@app.route('/predict',methods = ['POST'])
def predict(): # for rendering results on HTML GUI  
    int_features = [int(x) for x in request.form.values()]   #'request' will take input from all the form fields.
    final_features = [np.array(int_features)]
    prediction = lm_model.predict(final_features)
    
    output = round(prediction[0],2)
    
    return render_template('index.html', prediction_text = 'Predicted Employee Salary: $ {}'.format(output))

if __name__ == "__main__":  # this will run the complete flask
    app.run(debug=True)

