from flask import Flask # Import Flask Class
from flask import render_template

import random 

app = Flask(__name__) # Create an Instance

#Example of a route that passes
#data to a template
@app.route("/rand")
def randonnumber():
  i = random.randrange(100)
  return render_template("lucky.html",number = i)

#the "root" route
@app.route("/")
def index():
  return "<h1>Hello World from Repl.it!</h1>"

# return a template 
@app.route("/about")
def about():
  return render_template("about.html")

#return 
#example of static content
#like an image of includiong Class
@app.route("image_css")
  def image_css():
    return render_template("image_css.html")

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)

  
#@app.route('/') # Route the Function
#def main(): # Run the function
#	return 'Hello World'