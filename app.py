from flask import Flask, render_template,jsonify,request
import subprocess

app = Flask(__name__)
a = 2
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/button', methods=['POST'])
# def addbuttonlistener():
#     if request.method == 'POST':
#         action = request.json.get('action')
#         if action == 'abstract':
#             print("abstract")
#         elif action == 'mitre':
#             print("mitre")
#         elif action == 'security':
#             print("security")
#         else:
#             print("invalid")
        
#         return jsonify({'status': 'success'})

@app.route('/get', methods=['GET'])
def get_response():
    action = request.args.get('a')
    print("a: ",a )
    if action == '1':
        result = subprocess.run(['/usr/bin/python3', 'hello.py', 'yee'], capture_output=True, text=True)
        response = result.stdout
        print(response)
    elif action == '2':
        result = subprocess.run(['/usr/bin/python3', 'hello.py', 'param1'], capture_output=True, text=True)
        response = result.stdout
    elif action == '3':
        result = subprocess.run(['/usr/bin/python3', 'hello.py', 'param1'], capture_output=True, text=True)
        response = result.stdout
    else:
        response = "invalid action"           
    bot_response = response
    
    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)
