#Importing flask module in the project
from flask import Flask,render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/activity")
def activity():
    name = "Fritz"
    return render_template('index.html',index_variable = name)

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

#run the application on local server
app.run()
