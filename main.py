from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Kunal, how are you"

@app.route('/test')
def test():
    return jsonify({"message": "This is a test API endpoint"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
