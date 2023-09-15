from flask import Flask
import json
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/get_data")
def getdata():
    data = {
        'Name' : 'Bhanuprakash N R',
        'Employee No' : '12310'
    }
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081) 
