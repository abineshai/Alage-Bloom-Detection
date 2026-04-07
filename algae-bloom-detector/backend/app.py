import os
import traceback
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

@app.route('/api/detect', methods=['POST', 'GET'])
def detect():
    if request.method == 'GET':
        return jsonify({'status': 'AlgaeWatch running'})
    try:
        data = request.get_json(force=True)
        bbox = data.get('bbox')
        start_date = data.get('start_date', '2022-01-01')
        end_date = data.get('end_date', '2022-01-31')
        cloud_cover = data.get('cloud_cover', 20)
        scale = data.get('scale', 100)
        from services.algae_detection import run_algae_detection
        result = run_algae_detection(bbox=bbox, start_date=start_date, end_date=end_date, cloud_cover=cloud_cover, scale=scale)
        return jsonify(result), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/api/results/<filename>', methods=['GET'])
def serve_result(filename):
    path = os.path.join(RESULTS_DIR, os.path.basename(filename))
    if not os.path.exists(path):
        return jsonify({'error': 'not found'}), 404
    return send_file(path, mimetype='image/png')

@app.route('/api/download/<filename>', methods=['GET'])
def download(filename):
    path = os.path.join(RESULTS_DIR, os.path.basename(filename))
    if not os.path.exists(path):
        return jsonify({'error': 'not found'}), 404
    return send_file(path, mimetype='image/png', as_attachment=True, download_name=os.path.basename(filename))

if __name__ == '__main__':
    print('AlgaeWatch running on http://localhost:5001')
    app.run(debug=False, host='0.0.0.0', port=5001)
