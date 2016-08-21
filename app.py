
from flask import Flask, render_template, request, url_for
from datetime import datetime, date, time
import sqlite3 as sql

# Initialize the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def form():
    return render_template('form_submit.html')


@app.route('/hello/', methods=['POST'])


# Calculate the week of concievement, and get that year and week from database, and return that listing. 
def hello():
    
    pregnancy = 40 #pregnancy is 40 weeks. 

    #getting info from form
    year_test=request.form['chosenyear']
    month_test=request.form['chosenmonth']
    day_test=request.form['chosenday']

    year = int(year_test)
    month = int(month_test)
    day = int(day_test)
    week = date(year, month, day).isocalendar()[1]
    
    con = sql.connect("toplist3.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from listing")
    rows = cur.fetchall();


    if week < pregnancy: 
    	new_week = 52 + (week - pregnancy)
    	year = year - 1      


    	return render_template('form_action.html', year=year, new_week=new_week, rows = rows)

    
    else:
    	new_week = week - pregnancy
       

    	return render_template('form_action.html', year=year, new_week=new_week)
    

# Run the app :)
if __name__ == '__main__':
  app.run()
