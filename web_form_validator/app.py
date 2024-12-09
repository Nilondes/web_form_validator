from flask import Flask
from flask import request
from flask import render_template
from flask_tinydb import TinyDB
from functions import find_template

app = Flask(__name__)
db = TinyDB(app).get_db()


@app.route('/')
def home():
    return render_template('testform.html')


@app.route('/get_form', methods=['POST'])
def get_form():
    form = request.form.to_dict()
    result = find_template(db, form)
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')