from flask import Flask,render_template,request,make_response,jsonify
import mysql.connector
import json
import numpy as np
from werkzeug.utils import secure_filename
import os
import csv
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm

from sklearn.neighbors import KNeighborsClassifier
from flask_cors import CORS, cross_origin

app=Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dataloader')
def dataloader():
    return render_template('dataloader.html')




@app.route('/regdata')
def regdata():
    nm=request.args['stname']
    em=request.args['email']
    ph=request.args['phone']
    gen=request.args['gender']
    addr=request.args['addr1']
    pwd=request.args['pswd']
    connection = mysql.connector.connect(host='localhost',database='dsdb',user='root',password='Kavan123')
    sqlquery="insert into userdata(uname,email,phone,gender,addr,pswd) values('"+nm+"','"+em+"','"+ph+"','"+gen+"','"+addr+"','"+pwd+"')"
    print(sqlquery)
    cursor = connection.cursor()
    try:
        cursor.execute(sqlquery)
    except mysql.connector.IntegrityError:
        msg="Email already exist"
        resp=json.dumps(msg)
        return resp
    connection.commit()
    cursor.close()
    connection.close()
    msg="Data Saved Successfully"
    resp=json.dumps(msg)
    return resp


@app.route('/logdata')
def logdata():
    em=request.args['email']
    pwd=request.args['pswd']
    msg=''
    connection = mysql.connector.connect(host='localhost',database='dsdb',user='root',password='Kavan123')
    if(em =="admin@gmail.com"):
        sqlquery="select count(*) from userdata where email='"+em+"' and pswd='"+pwd+"'"
        cursor = connection.cursor()
        cursor.execute(sqlquery)
        data=cursor.fetchall()
        if data[0][0]>0:
            msg='admin'
        else:
            msg='failure'
    else:
        sqlquery="select count(*) from userdata where email='"+em+"' and pswd='"+pwd+"'"
        cursor = connection.cursor()
        cursor.execute(sqlquery)
        data=cursor.fetchall()
        if data[0][0]>0:
            msg='success'
        else:
            msg='failure'
    print(sqlquery)
    cursor.close()


    connection.close()
    resp=json.dumps(msg)
    return resp



from flask import Flask, render_template, request, jsonify
import mysql.connector
import joblib
import numpy as np



# MySQL configurations
mysql_config = {
    'host': 'localhost',
    'database': 'dsdb',
    'user': 'root',
    'password': 'Kavan123'
}

# Load the trained model and scaler
model = joblib.load('decision_tree_model.pkl')
scaler = joblib.load('scaler.pkl')

# Endpoint for rendering the prediction form
@app.route('/predict')
def predict():
    return render_template('predict.html')

# Endpoint for processing prediction and saving data
@app.route('/predictdata', methods=['POST'])
def predictdata():
    if request.method == 'POST':
        # Extract features from the form data
        system_perc = float(request.form['system_perc'])
        wait_perc = float(request.form['wait_perc'])
        avg_1_min = float(request.form['avg_1_min'])
        free_mb = float(request.form['free_mb'])
        in_bytes_sec = float(request.form['in_bytes_sec'])
        out_packets_sec = float(request.form['out_packets_sec'])

        # Prepare the feature array and scale it
        features = np.array([[system_perc, wait_perc, avg_1_min, free_mb, in_bytes_sec, out_packets_sec]])
        features_scaled = scaler.transform(features)

        # Predict using the loaded model
        prediction_code = model.predict(features_scaled)[0]
        prediction = 'malicious' if prediction_code == 1 else 'normal'

        # Insert the data into the MySQL database
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()

        try:
            cursor.execute(
                "INSERT INTO botattack_data (system_perc, wait_perc, avg_1_min, free_mb, in_bytes_sec, out_packets_sec, prediction) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (system_perc, wait_perc, avg_1_min, free_mb, in_bytes_sec, out_packets_sec, prediction)
            )
            connection.commit()
            msg = "Prediction and Data Saved Successfully"
        except Exception as e:
            connection.rollback()
            msg = f"Error occurred while saving data: {e}"
        finally:
            cursor.close()
            connection.close()

        # Return JSON response with prediction and message
        return jsonify(prediction=prediction, msg=msg)


if __name__ == '__main__':
    app.run(debug=True)



