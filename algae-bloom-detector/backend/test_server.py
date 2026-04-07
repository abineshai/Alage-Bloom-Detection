from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/detect', methods=['GET','POST'])
def detect():
    return jsonify({'status': 'ok'})
app.run(host='0.0.0.0', port=5001)
