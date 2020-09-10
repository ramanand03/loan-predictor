from flask import Flask, render_template, request, url_for, redirect
from joblib import load
import numpy as np
app = Flask(__name__)

model = load("newmodel.joblib")
@ app.route('/')
def home():
    return render_template("index.html")

@ app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
         df = []
         df.append( int(request.form['Gender']))
         df.append(int(request.form['Married']))
         df.append(int(request.form['NotEducated']))
         df.append(int(request.form['Self Employe']))
         df.append(float(request.form['Loan Amount']))
         df.append(float(request.form['Loan C. History']))
         df.append(float(request.form['Applicant_Income']))
         df.append(float(request.form['Co-App. Income']))
         df.append(int(request.form['Property Area']))
         df.append(int(request.form['Dependents']))
         df.append(int(request.form['Loan Amt Term']))

         prediction = model.predict([df])         

         if prediction[0] == 0:
             return render_template("result0.html")
         else :
             return render_template("result1.html")

if __name__ == "__main__":
    app.run(debug=True)