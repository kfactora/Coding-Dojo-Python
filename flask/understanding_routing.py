from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("initialized the WORLD!")
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    print("initialized the DOJO!")
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    print("initialized FLASK!")
    return 'Hi '+name

@app.route('/repeat/<number>/<name>')
def repeat(name, number):
    print("initialized the REPEAT!")
    return name*int(number)

if __name__=="__main__":
    app.run(debug=True)
