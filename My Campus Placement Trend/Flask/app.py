from flask import Flask, request, render_template,redirect,url_for
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np
import pandas as pd
import joblib 
import pickle

app = Flask(__name__)
model1 =pickle.load(open('mytrainedplacement_model.pkl',"rb")) 
ct=joblib.load("mytrainedplacement_model.pkl") 

@app.route('/')
def hel():
    return render_template("current.html")

@app.route('/job')
def jobs():
     return render_template("joblist.html")

@app.route('/login')
def log():
    return render_template("login.html")

@app.route('/resume')
def resume():
    return render_template("resum.html")

@app.route('/interview')
def interview():
    return render_template("interview.html")
@app.route('/career')
def career():
  return render_template("careers.html")

@app.route('/sec')
def hello():
    return render_template("index.html") 

@app.route('/guest', methods=['GET','POST'])
def Guest():
    if request.method == 'POST':
        
        student_id = request.form['student_id']
        gender = request.form['gender']
        age = request.form['age']
        education = request.form['education']
        cgpa = request.form['cgpa']
        internships = request.form['internships']
        projects = request.form['projects']
        recommendation = request.form['recommendation']
        specialization = request.form['specialization']
        backlogs = request.form['backlogs']
    return render_template("index2.html")


@app.route('/y_predict', methods=["POST"])
def y_predict():
    # Collect form values from the request
    student_id = int(request.form['student_id'])
    gender = int(request.form['gender'])
    age = int(request.form['age'])  # Convert to integer
    education = int(request.form['education'])  # Convert to integer
    cgpa = float(request.form['cgpa'])  # Convert to float
    internships = int(request.form['internships'])  # Convert to integer
    projects = int(request.form['projects'])  # Convert to integer
    recommendation = int(request.form['recommendation'])  # Convert to integer
    specialization = int(request.form['specialization'])  # Convert to integer
    backlogs = int(request.form['backlogs'])  # Convert to integer
    
    # Prepare the input feature array
    x_test = [student_id, gender, age, education, cgpa, internships, projects, recommendation, specialization, backlogs]
    
    # Convert the feature array to a numpy array
    x_test = np.array(x_test).reshape(1, -1)
    
    # Make a prediction using the loaded model
    predict_output = model1.predict(x_test)
    
    if predict_output == 0:
        return render_template("unsel.html")
    else:
        return render_template("sel.html")

if __name__=="__main__":

 app.run(debug=True,port=8000)

