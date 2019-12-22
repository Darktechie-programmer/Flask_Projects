from flask import Flask,render_template,request
# from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
import pymysql as sql
# import json

# with open('config.json','r') as c:
#     params = json.load(c)["params"]

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:81/techieblog'
#db = SQLAlchemy(app)
"""
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20),nullable=False)"""


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        '''add entry to the databases...'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        #entry = Contacts(name=name,phone_num=phone,msg=message,date=datetime.now(),email=email)
        # db.session.add(entry)
        # db.session.commit()
        date = datetime.now()
        try:
            db = sql.connect(host = "localhost",port = 3306,user = "root",password = "123",database=" techieblog")
            mycursor = db.cursor()
            entry = "insert into contacts values('{}','{}','{}','{}','{}')".format(name,phone,message,date,email)
            mycursor.execute(entry) 
            db.commit()  
        except Exception as e:
            return render_template("contact.html",error=e)
    return render_template("contact.html")


app.run(debug=True)

