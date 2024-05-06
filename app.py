from flask import Flask, render_template
import awsgi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

def handler(event, context):
    return awsgi.response(app, event, context)