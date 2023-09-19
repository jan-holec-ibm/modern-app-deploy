from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    import os                           
    greeting = os.getenv('HELLO_STR', "Docker")
    
    return '<h1>Hello from ' + greeting + '</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)