from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import os
app = Flask(__name__, template_folder=os.getcwd() + "/web", root_path=os.getcwd())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        a = request.form['left']
        b = request.form['right']
        c = int(a) + int(b)        
        return render_template('index.html', RESULT = str(c))
    return render_template('index.html')

if __name__ == "__main__":
    app.run()