from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime
from bokeh.plotting import figure, show, output_file
import dill

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
  gender = '  '
  if request.method == 'GET':
    return render_template('index.html',output=gender)
  elif request.method == 'POST':
    gender = request.form.get('sex')
    poverty = request.form.get('poverty')
    school = request.form.get('school')
    marital = request.form.get("marital")
    race = request.form.get("race")
    orient = request.form.get("orient")
    phys = request.form.get("phys")
    drinks = request.form.get("drinks")
    age = request.form.get("age")
    output = get_risk([phys,orient,school,drinks,race,poverty,marital,gender,age])
    if output ==0:
      message = "Not At Risk"
    elif output == 1:
      message = "At Risk!"
    return render_template('index.html',output=message)



def get_risk(features):
  forest = dill.load(open('forest.pkd','rb'))
  return forest.predict(features)
  
  












if __name__ == '__main__':
  app.run(port=33507)
