from flask import Flask, render_template
import subprocess

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    result = subprocess.check_output(['python', 'main.py'], universal_newlines=True)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
