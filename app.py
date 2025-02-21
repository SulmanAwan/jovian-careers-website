from flask import Flask, render_template, jsonify

app = Flask(__name__) #importing a class and creating an instance of the class

#list of dictionaries in JSON format (simulates a database)
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Deli, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

@app.route('/') #maps to the homepage of jovian.com, when the url / is accessed run hello_world.
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

#a url that doesn't return html, but returns structured data in the form of JSON which can be programatically analyzed.
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True) #Host 0.0.0.0 means it will be run from the local machine.