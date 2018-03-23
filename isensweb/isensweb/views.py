"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from isensweb import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'isensdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM patient_record"
    cursor.execute(sql)
    patientrecords = cursor.fetchall()
    patientrows = len(patientrecords)
    patientcolumns = len(patientrecords[0])
    #print(patientrecords)
    sql = "SELECT * FROM patient_result"
    cursor.execute(sql)
    patientresultsrecords = cursor.fetchall()
    #print(patientresultsrecords)
    patientresultsrows = len(patientresultsrecords)
    patientresultscolumns = len(patientresultsrecords[0])
    conn.close()

    return render_template(
        'about.html',
        title='Patient Record and Result',
        patients=patientrecords,
        rows=patientrows,
        columns=patientcolumns,
        results=patientresultsrecords,
        resultrows=patientresultsrows,
        resultcolumns=patientresultscolumns,
        year=datetime.now().year,
        message='View patient records here'
    )
