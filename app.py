from flask import Flask, render_template,jsonify,request
import subprocess
app = Flask(__name__)
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

@app.route('/get', methods=['POST'])
def get_response():
    data = request.json
    action = data.get('a')
    message = data.get('message')
    # print("a: ",type(action) )
    print("msg: ",message)
    if action == 1:
        result = subprocess.run(['/usr/bin/python3', 'flask_to_lambda.py', message, 'Summary_GenAI'], capture_output=True, text=True)
        response = result.stdout
        # print("result",result)
        print("response: ", response)
        print("error: ", result.stderr)
    elif action == 2:
        result = subprocess.run(['/usr/bin/python3', 'flask_to_lambda.py', message,'Mitre_attack_GenAI'], capture_output=True, text=True)
        response = result.stdout
        print("mitre: ",response)
    elif action == 3:
        result = subprocess.run(['/usr/bin/python3', 'flask_to_lambda.py', message, 'Cybersecurity_GenAI'], capture_output=True, text=True)
        response = result.stdout
    else:
        response = "invalid action"           
    bot_response = response
    
    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)
