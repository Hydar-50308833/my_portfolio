# app.py 
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine("postgresql://postgres:password@localhost:5432/db_project")
db = scoped_session(sessionmaker(bind=engine))

app.secret_key = '12345678'
#Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



@app.route("/form")
def form():    
    return render_template("form.html")

@app.route("/addform", methods=["POST"])
def addform():
    pname=request.form.get("pname")
    prole=request.form.get("prole")
    pdesc=request.form.get("pdesc")
  #  year=request.form.get("year")
    db.execute("INSERT INTO tb_project_info (pro_name,pro_role,pro_desc) VALUES (:pname,:prole,:pdesc)",
            {"pname": pname, "prole": prole, "pdesc":pdesc}) 
    db.commit() 
    # return render_template("index.html")
    return redirect(url_for('hello'))


  

# ....................................................
# Display entire website route
@app.route("/")
@app.route("/home")
def hello():
    # returning string
    name = "Hydar Hussain"
    plist = db.execute("SELECT * from tb_project_info")
    return render_template("index.html", plist = plist, name = name)


app.run(debug = True)

