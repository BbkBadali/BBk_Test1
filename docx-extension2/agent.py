
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # اجازه دسترسی از کروم اکستنشن

@app.route('/receive_filename', methods=['POST'])
def receive_filename():
    data = request.get_json()
    filename = data.get('filename')
    print(f"📄 Received filename: {filename}")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
