from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API running on port 7443!"})

@app.route('/api/example', methods=['GET'])
def example():
    return jsonify({"data": "This is an example endpoint."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7443)
