from flask import Flask, render_template

app = Flask(__name__) #importing a class and creating an instance of the class

@app.route('/') #maps to the homepage of jovian.com, when the url / is accessed run hello_world.
def hello_world():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True) #Host 0.0.0.0 means it will be run from the local machine.