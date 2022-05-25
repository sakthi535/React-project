from flask import Flask

app = Flask(__name__)

@app.route('/checkHere',methods=['GET'])
def checkHere():
    return {"I am":5}

if __name__ == "__main__" :
    app.run(debug = True)